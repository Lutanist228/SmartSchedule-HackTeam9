from django.contrib import admin
from schedule_app.models import MedEmployees, EmpDep, DepInfo

# Register your models here.

admin.site.register([MedEmployees, EmpDep, DepInfo])

