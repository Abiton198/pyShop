# from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return HttpResponse('Welcome, to the new Django Project')

# Create your views here.
