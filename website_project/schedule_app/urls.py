from django.urls import path
from . import views
from django.shortcuts import render 

urlpatterns = [
    path('', views.index),
    path('add_empl/', views.add_empl_pg, name="add_empl")
]
