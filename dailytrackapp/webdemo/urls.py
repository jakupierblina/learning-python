from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('homepage/', views.homepage, name='homepage'),
]
