# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome, to the new Django Project')

def new(request):
    return HttpResponse('This is my new pen shop!')

# Create your views here.
