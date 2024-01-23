# employee_app/urls.py
from django.urls import path
from .views import employee_list, add_employee, update_employee, delete_employee

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', add_employee, name='add_employee'),
    path('employees/<int:employee_id>/update/', update_employee, name='update_employee'),
    path('employees/<int:employee_id>/delete/', delete_employee, name='delete_employee'),
]
