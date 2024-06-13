from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import *
from .forms import *

# Create your views here.
def index(request):
    empl = MedEmployees.objects.values("first_name", "last_name", "patronymic")
    empl = {key + 1:f"{value['patronymic']} {value['first_name'][0]}.{value['last_name'][0]}." for key, value in enumerate(empl)}

    return render(request, "schedule_app/index.html", {"empl_dict": empl}) 

def add_empl_pg(request):
    empl = MedEmployees.objects.values("first_name", "last_name", "patronymic")
    empl = {key + 1:f"{value['patronymic']} {value['first_name'][0]}.{value['last_name'][0]}." for key, value in enumerate(empl)}
    
    if request.method == "POST":
        pers_form = AddEmployee(request.POST)
        if pers_form.is_valid():
            print(pers_form.cleaned_data)
    else:    
        pers_form = AddEmployee()
        
    return render(request, "schedule_app/empl_adding.html", {"pers_form":pers_form, "empl_dict": empl})

def add_dep_pg(request):
    empl = MedEmployees.objects.values("first_name", "last_name", "patronymic")
    empl = {key + 1:f"{value['patronymic']} {value['first_name'][0]}.{value['last_name'][0]}." for key, value in enumerate(empl)}
    
    if request.method == "POST":
        dep_form = DepInfo(request.POST)
        if dep_form.is_valid():
            print(dep_form.cleaned_data)
    else:    
        dep_form = DepInfo()

    return render(request, "schedule_app/dep_adding.html", {"dep_form":dep_form, "empl_dict": empl})

