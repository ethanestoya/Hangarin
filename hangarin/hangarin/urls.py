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
from django.urls import path, include
from taskmanager import views
from taskmanager.views import HomePageView, TasksView, TasksCreateView, TasksUpdateView, TasksDeleteView, SubTasksView, SubtasksCreateView, SubtasksUpdateView, SubtasksDeleteView, CategoriesView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, PrioritiesView, NotesView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', views.HomePageView.as_view(), name='home'),
    
    # Task Model
    path('task_list/', TasksView.as_view(), name='task-list'),
    path('task_list/add/', TasksCreateView.as_view(), name='task-add'),
    path('task_list/<int:pk>/', TasksUpdateView.as_view(), name='task-update'),
    path('task_list/<int:pk>/delete/', TasksDeleteView.as_view(), name='task-delete'),

    # SubTask Model
    path('subtask_list/', SubTasksView.as_view(), name='subtask-list'),
    path('subtask_list/add/', SubtasksCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<int:pk>/', SubtasksUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<int:pk>/delete/', SubtasksDeleteView.as_view(), name='subtask-delete'),

    # Category Model
    path('category_list/', CategoriesView.as_view(), name='category-list'),
    path('category_list/add/', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # Priority Model
    path('priority_list/', PrioritiesView.as_view(), name='priority-list'),
    
    # Note Model
    path('notes_list/', NotesView.as_view(), name='notes-list'),
    path('notes_list/add/', NoteCreateView.as_view(), name='note-add'),
    path('notes_list/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('notes_list/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),

]
