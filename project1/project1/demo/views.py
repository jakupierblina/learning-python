from django.shortcuts import render
from django.http import HttpResponse

'''
    used to show the pages, to return a view after every every action is been performed in website
'''

# Create your views here.

def homepage(request):
    return render(request, 'demo/index.html')
    # return render( request, 'index.html')


def about(request):
    return render(request, 'demo/about.html')
    # return render(request, 'about.html')
    # return HttpResponse('<h1> Welcome to my homepage!</h1>')



def gettingstarted(request):
    return render(request, 'demo/mission.html')


def material(request):
    return render(request, 'demo/introduction.html')