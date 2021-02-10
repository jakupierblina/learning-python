from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup



def homepage(request):
    template ='webdemo/index.html'
    #get the input

    city = request.POST.get('city')
    print(city)
    return render(request, template,{'form' : city})