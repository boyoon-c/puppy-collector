"""
from django.http import HttpResponse

Create your views here.
def home(request):
    return HttpResponse('<h1>HOME</h1>')

def about(request):
    return HttpResponse('<h1>ABOUT</h1>')
"""

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Puppies:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

puppies = [
  Puppies('Charles', 'Golden Retriever', 'Very playful.', 1),
  Puppies('Bob', 'Golden Retriever', 'Very cute', 0),
  Puppies('Winky', 'Golden Retriever', 'Very energetic', 4),
  Puppies('Rocky', 'Golden Retriever', 'Loves strangers', 6)
]

def puppies_index(request):
  return render(request, 'puppies/index.html', { 'puppies': puppies })