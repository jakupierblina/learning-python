from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'webdemo/base.html')

def login(request):
    return render(request, 'webdemo/login.html')


def register(request):
    return render(request, 'webdemo/register.html')