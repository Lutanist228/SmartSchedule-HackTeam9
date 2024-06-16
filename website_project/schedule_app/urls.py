from django.urls import path
from . import views
from django.shortcuts import render 

urlpatterns = [
    path('', views.index),
    path('add_empl/', views.add_empl_pg, name="add_empl"),
    path('add_dep/', views.add_dep_pg, name="add_dep"),
    path('empl_pg/<int:empl_id>/', views.empl_proc, name="empl_proc")
]
