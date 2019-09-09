from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'homepage.html')
# Create your views here.

def about(request):
    return render(request, 'about.html')

def cv(request):
        return render(request, 'cv.html')

def contact(request):
        return render(request, 'contact.html')
