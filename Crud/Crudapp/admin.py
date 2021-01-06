from django.contrib import admin
from .models import Payroll,Team,Employee

# Register Payroll model 
admin.site.register(Payroll)

# Register Teams model
admin.site.register(Team)

# Register Employee model
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Name','Employee_Id','Teams','Hourly_rate','Month','Year','Monthly_salary']
admin.site.register(Employee, EmployeeAdmin)



