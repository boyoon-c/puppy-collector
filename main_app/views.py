"""
from django.http import HttpResponse

Create your views here.
def home(request):
    return HttpResponse('<h1>HOME</h1>')

def about(request):
    return HttpResponse('<h1>ABOUT</h1>')
"""

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Puppy, Toy
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def puppies_index(request):
  puppies = Puppy.objects.all()
  return render(request, 'puppies/index.html', {'puppies': puppies })

@login_required
def puppies_detail(request, pup_id):
  puppy = Puppy.objects.get(id=pup_id)
  toys_puppy_doesnt_have = Toy.objects.exclude(id__in = puppy.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', { 
    'puppy': puppy,
    'feeding_form': feeding_form,
    'toys': toys_puppy_doesnt_have})

class PuppyCreate(LoginRequiredMixin, CreateView):
  model = Puppy
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/puppies/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PuppyUpdate(LoginRequiredMixin, UpdateView):
  model = Puppy
  fields = ['breed', 'description', 'age']
  success_url = '/puppies/'

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies/'

@login_required
def add_feeding(request, pup_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.puppy_id = pup_id
    new_feeding.save()
  return redirect('puppies_detail', pup_id)

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, pup_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Puppy.objects.get(id=pup_id).toys.add(toy_id)
  return redirect('puppies_detail', pup_id)

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('puppies_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)