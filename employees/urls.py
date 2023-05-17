from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_employees, name='employees'),    
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employee/edit/<int:id>/', views.employee_edit_data, name='edit'),
    path('delete_employee/<int:id>', views.delete_employee, name="delete_employee"),
    path('create-user/', views.create_user, name='create_user'),
    path('users/all/', views.all_users, name='all_users'),
    path('user-profile/', views.user_profile, name='userprofile'),
]