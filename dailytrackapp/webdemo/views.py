from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import OrderForm, CreateUserForm

# Create your views here.
def welcome(request):
    return render(request, 'webdemo/base.html')

def login(request):
    return render(request, 'webdemo/register/login.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'webdemo/register/register.html', context)




def homepage(request):
    return render(request, 'webdemo/authorized/homepage.html')

