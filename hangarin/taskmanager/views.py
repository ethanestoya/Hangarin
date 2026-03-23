from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from taskmanager.models import Category, Priority, Task, Note, SubTask
from taskmanager.forms import TaskForm, SubTaskForm, CategoryForm, NoteForm
# Create your views here.
# List View
class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = 'home.html'

class TasksView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_list.html'
    paginate_by = 5

class SubTasksView(ListView):
    model = SubTask
    context_object_name = 'subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5

class CategoriesView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
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
class TasksCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class SubtasksCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

# Update View
class TasksUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class SubtasksUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

# Delete View
class TasksDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

class SubtasksDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')