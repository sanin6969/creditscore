from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("register/",Register,name='register'),
    path("login/",Login,name='login'),
]
