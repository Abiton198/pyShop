from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def new(request):
    return HttpResponse('This is my new fruit shop!')

# Create your views here.
