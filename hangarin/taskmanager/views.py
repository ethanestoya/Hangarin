from django.shortcuts import render
from django.views.generic.list import ListView
from taskmanager.models import Category, Priority, Task, Note, SubTask

# Create your views here.
# List View
class HomePageView(ListView):
    model = Category
    context_object_name = 'home'
    template_name = 'home.html'

