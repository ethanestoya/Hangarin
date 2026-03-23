from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from taskmanager.models import Category, Priority, Task, Note, SubTask

# Create your views here.
# List View
class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = 'home.html'

class TasksView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task-list.html'
    paginate_by = 5

class SubtasksView(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5

class CategoriesView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.view'
    paginate_by = 5

class PrioritiesView(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 5

class NotesView(ListView):
    model = Note
    context_object_name = 'note'
    template_name = 'note_list.html'
    paginate_by = 5

# Create View
class 

# Update View

# Delete View
