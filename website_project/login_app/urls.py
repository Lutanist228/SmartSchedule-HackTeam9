from django.urls import path
from . import views
from django.shortcuts import render
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('manager/', include('schedule_app.urls'),)
]
