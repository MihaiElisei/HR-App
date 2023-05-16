from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_employees, name='employees'),    
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employee/edit/<int:id>/', views.employee_edit_data, name='edit'),
]