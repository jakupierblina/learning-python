from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('chat/', views.chat, name='chat'),

    #section's
    path('diary/', views.diary, name='diary_section'),
    path('todo/', views.todo, name='todo_section'),
    path('calendar/', views.calendar, name='calendar_section'),
]
