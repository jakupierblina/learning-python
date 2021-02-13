from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .form import OrderForm, CreateUserForm

# Create your views here.
def welcome(request):
    return render(request, 'webdemo/base.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')

           user = authenticate(request, username=username, password=password)

           if user is not None:
                login(request, user)
                return redirect('homepage')
           else:
               messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'webdemo/register/login.html', context)



def logoutUser(request):
	logout(request)
	return redirect('login')


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account '+ user + ' was created succesfully!')
            return redirect('login')
    context = {'form': form}
    return render(request, 'webdemo/register/register.html', context)




def homepage(request):
    return render(request, 'webdemo/authorized/homepage.html')


#section's
def diary(request):
    return render(request, 'webdemo/authorized/partials/_section_diary.html')


def todo(request):
    return render(request, 'webdemo/authorized/partials/_section_todo.html')

def calendar(request):
    return render(request, 'webdemo/authorized/partials/_section_calendar.html')