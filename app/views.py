from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic import CreateView

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'
