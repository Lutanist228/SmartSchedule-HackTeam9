from django import forms
from .models import *

class AddEmployee(forms.ModelForm):
    # name_field = forms.CharField(max_length=255, label="Имя")
    # surname = forms.CharField(max_length=255, label="Фамилия")
    # patronymic = forms.CharField(max_length=255, label="Отчество")
    # snils = forms.CharField(max_length=255, label="СНИЛС")
    attach_to_dep = forms.ModelChoiceField(queryset=DepInfo.objects.values("id"), label="Идентификатор Отдела")

    class Meta:
        model = MedEmployees
        fields = "__all__"
    
class DepInfo(forms.ModelForm): 
    # department_name = forms.CharField(max_length=600, label="Название департамента")
    # job_title = forms.CharField(max_length=255, label="Название должности")
    # job_phone = forms.CharField(max_length=255, label="Рабочий телефон")

    class Meta:
        model = DepInfo
        fields = "__all__"