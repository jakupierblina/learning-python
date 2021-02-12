from django.shortcuts import render
from django.contrib.auth.forms import  UserCreationForm
# Create your views here.
def welcome(request):
    return render(request, 'webdemo/base.html')

def login(request):
    return render(request, 'webdemo/register/login.html')


def register(request):
    return render(request, 'webdemo/register/register.html')




def homepage(request):
    return render(request, 'webdemo/authorized/homepage.html')

