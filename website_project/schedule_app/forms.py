from django import forms
from .models import *

class AddEmployee(forms.Form):
    name_field = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    patronymic = forms.CharField(max_length=255)
    snils = forms.CharField(max_length=255)




