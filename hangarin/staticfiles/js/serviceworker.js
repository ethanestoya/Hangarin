// Cache version
const CACHE_NAME = 'hangarin-cache-v1';

// Assets to cache on install
const ASSETS_TO_CACHE = [
  '/',
  '/static/css/bootstrap.min.css',
  '/static/css/ready.css',
  '/static/css/demo.css',
  '/static/js/core/jquery.3.2.1.min.js',
  '/static/js/core/popper.min.js',
  '/static/js/core/bootstrap.min.js',
  '/static/js/plugin/chartist/chartist.min.js',
  '/static/js/plugin/chartist/plugin/chartist-plugin-tooltip.min.js',
  '/static/js/plugin/bootstrap-notify/bootstrap-notify.min.js',
  '/static/js/plugin/bootstrap-toggle/bootstrap-toggle.min.js',
  '/static/js/plugin/jquery-mapael/jquery.mapael.min.js',
  '/static/js/plugin/jquery-mapael/maps/world_countries.min.js',
  '/static/js/plugin/chart-circle/circles.min.js',
  '/static/js/plugin/jquery-scrollbar/jquery.scrollbar.min.js',
  '/static/js/ready.min.js',
  '/static/img/profile.jpg',
  '/static/img/profile2.jpg',
  '/static/img/menu.png',
  '/static/img/menu2.png',
  '/static/img/icon-192.png',
  '/static/img/icon-512.png',
];

// Install event: cache critical assets
self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(ASSETS_TO_CACHE)
        .then(() => self.skipWaiting())
        .catch(err => console.error('Cache addAll error:', err));
    })
  );
});

// Activate event: clean up old caches
self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (cacheNames) {
      return Promise.all(
        cacheNames.map(function (cacheName) {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      ).then(() => self.clients.claim());
    })
  );
});

// Fetch event: cache-first strategy with network fallback
self.addEventListener('fetch', function (e) {
  // Skip non-GET requests
  if (e.request.method !== 'GET') {
    return;
  }

  e.respondWith(
    caches.match(e.request)
      .then(function (response) {
        // Return cached response if available
        if (response) {
          return response;
        }
        
        // Otherwise fetch from network
        return fetch(e.request)
          .then(function (networkResponse) {
            // Don't cache non-successful responses
            if (!networkResponse || networkResponse.status !== 200 || networkResponse.type === 'error') {
              return networkResponse;
            }
            
            // Cache successful responses for future use
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then(function (cache) {
              cache.put(e.request, responseClone);
            });
            
            return networkResponse;
          })
          .catch(function () {
            // Return cached version if network fails
            return caches.match(e.request)
              .then(function (cachedResponse) {
                return cachedResponse || new Response('Offline - content not available', {
                  status: 503,
                  statusText: 'Service Unavailable',
                  headers: new Headers({
                    'Content-Type': 'text/plain'
                  })
                });
              });
          });
      })
  );
});
