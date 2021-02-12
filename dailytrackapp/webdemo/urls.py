from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('homepage', views.homepage, name='homepage'),
]
