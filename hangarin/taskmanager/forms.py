from django.forms import ModelForm
from django import forms
from .models import Task, SubTask, Category, Note

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'categoryFK', 'priorityFK']

class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = ['parentTaskFK', 'title', 'status']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['taskFK','content']