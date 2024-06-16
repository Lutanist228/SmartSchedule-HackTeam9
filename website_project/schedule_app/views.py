from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from .models import *
from .forms import *
from .inner_scripts.additional_functions import * 

# Create your views here.
def index(request):
    empl = empl_display()

    return render(request, "schedule_app/index.html", {"empl_dict": empl}) 

def add_empl_pg(request):
    empl = empl_display()
    
    if request.method == "POST":
        pers_form = AddEmployee(request.POST)
        if pers_form.is_valid():
            pers_form.save() # сохранение в бд
            print(pers_form.cleaned_data)
            return redirect('add_empl')
    else:    
        pers_form = AddEmployee()
                
    return render(request, "schedule_app/empl_adding.html", {"pers_form":pers_form, "empl_dict": empl})

def add_dep_pg(request):
    empl = empl_display()
    
    if request.method == "POST":
        dep_form = DepInfo(request.POST)
        if dep_form.is_valid():
            dep_form.save()
            print(dep_form.cleaned_data)
            return redirect('')
    else:    
        dep_form = DepInfo()

    return render(request, "schedule_app/dep_adding.html", {"dep_form":dep_form, "empl_dict": empl})

def empl_proc(request, empl_id):
    all_empl, curr_empl = empl_display(), empl_display(False, empl_id)
    
    return render(request, "schedule_app/empl_table.html", {"empl_dict": all_empl, "curr_empl": curr_empl}) 
    
    
    

