from ..models import *

def empl_display(all_empl: bool = True, empl_id: int = None):
    if all_empl == True:
        empl_fio = MedEmployees.objects.values("first_name", "last_name", "patronymic")
        empl_fio = {key + 1:f"{value['last_name']} {value['first_name'][0]}.{value['patronymic'][0]}." for key, value in enumerate(empl_fio)}
        return empl_fio
    else:
        empl_fio = MedEmployees.objects.values("first_name", "last_name", "patronymic")
        empl_fio = {key + 1:f"{value['last_name']} {value['first_name'][0]}.{value['patronymic'][0]}." for key, value in enumerate(empl_fio)}
        empl_fio = empl_fio.get(empl_id)
        return empl_fio
    
