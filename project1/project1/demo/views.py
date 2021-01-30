from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
    return render(request, 'demo/index.html')
    #return render( request, 'index.html')

def material(request):
    return render(request, 'demo/material.html')
    #return render(request, 'material.html')

def getting(request):
    return render(request, 'demo/gettingstarted.html')
    #return render( request, 'gettingstarted.html')

def about(request):
    return render(request, 'demo/about.html')
    #return render(request, 'about.html')
    #return HttpResponse('<h1> Welcome to my homepage!</h1>')
