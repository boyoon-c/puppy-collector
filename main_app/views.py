from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>HOME</h1>')

# def about(request):
#     return HttpResponse('<h1>ABOUT</h1>')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
