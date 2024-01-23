from django.contrib import admin
from employeeapp.models import Department, Employee, EmployeeSalary
# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)