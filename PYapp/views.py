from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')
def schedule(request):
    return render(request, 'schedule.html')
def classes(request):
    return render(request, 'classes.html')