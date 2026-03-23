"""
URL configuration for hangarin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taskmanager import views
from taskmanager.views import HomePageView, TasksView, SubtasksView, CategoriesView, PrioritiesView, NotesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('task-list', TasksView.as_view(), name='task-list'),
    path('subtask_list', SubtasksView.as_view(), name='subtask-list'),
    path('category_list', CategoriesView.as_view(), name='category-list'),
    path('priority_list', PrioritiesView.as_view(), name='priority-list'),
    path('notes_list', NotesView.as_view(), name='notes-list'),
]
