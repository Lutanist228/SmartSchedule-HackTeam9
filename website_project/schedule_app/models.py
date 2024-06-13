from django.db import models

# Create your models here.
class MedEmployees(models.Model):
    first_name = models.CharField("имя", max_length=250)
    last_name = models.CharField("фамилия", max_length=250)
    patronymic = models.CharField("отчество", max_length=250)
    snils = models.CharField("снилс", default="000-000-000 00", max_length=50)
    
    def __str__(self) -> str:
                return self.first_name 

    class Meta:
            verbose_name = 'Employee Block'
            verbose_name_plural = 'Employees Blocks'
    
class DepInfo(models.Model):
    department_name = models.CharField("название департамента", max_length=500)
    job_title = models.CharField("наименование должности", max_length=200)
    job_phone = models.CharField("рабочий телефон", max_length=50)
    
    def __str__(self) -> str:
                return self.department_name 

    class Meta:
            verbose_name = 'Department Block'
            verbose_name_plural = 'Departments Blocks'
    
class EmpDep(models.Model):
    department = models.ForeignKey('DepInfo', on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey('MedEmployees', on_delete=models.SET_NULL, null=True)
    
    class Meta:
            verbose_name = 'Emp-Dep Block'
            verbose_name_plural = 'Emp-Dep Blocks'
            