from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request


def homepage(request):
    if request.method == 'POST':
        #get the input
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                    city + '&units=metric&appid=70e11144074217e98ad2cb2d334860f3').read()

        list_of_data = json.loads(source)
        data ={
        "temp": str(list_of_data['main']['temp'])+'C',
        "main": str(list_of_data['weather'][0]['main']),
        }

        # temperature='24C'
         #convert json
         #r = request.get(url.format(city)).json()
        #print(data)
    else:
        #return HttpResponse('<h1>Page not found</h1>')
        data = {}

    return render(request, 'webdemo/index.html',data)