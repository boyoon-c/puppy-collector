"""
from django.http import HttpResponse

Create your views here.
def home(request):
    return HttpResponse('<h1>HOME</h1>')

def about(request):
    return HttpResponse('<h1>ABOUT</h1>')
"""

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Puppy

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def puppies_index(request):
  puppies = Puppy.objects.all()
  return render(request, 'puppies/index.html', {'puppies': puppies })

def puppies_detail(request, pup_id):
  puppy = Puppy.objects.get(id=pup_id)
  return render(request, 'puppies/detail.html', { 'puppy': puppy })

class PuppyCreate(CreateView):
  model = Puppy
  fields = '__all__'
  success_url = '/puppies/'

class PuppyUpdate(UpdateView):
  model = Puppy
  fields = ['breed', 'description', 'age']
  success_url = '/puppies/'

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies/'