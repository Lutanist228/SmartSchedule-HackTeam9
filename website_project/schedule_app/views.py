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
    form = AddEmployee()
        
    return render(request, "schedule_app/empl_adding.html", {"form":form, "empl_dict": empl})

