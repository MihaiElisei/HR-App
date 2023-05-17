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
    path('employee/profile/<int:id>/', views.user_detail, name='employeeinfo'),
    path('users/<int:id>/block', views.block_users, name='block_users'),
    path('users/<int:id>/unblock', views.unblock_users, name='unblock_users'),
    path('emergency/create/', views.emergency_form, name='emergency_form'),
    path('emergency/edit/<int:id>', views.emergency_edit, name='emergency_edit'),
    path('family/create/', views.family_form, name='family_form'),
    path('family/edit/<int:id>', views.family_edit, name='family_edit'),
    path('bank/create/', views.bank_form, name='bank_form'),
    path('bank/edit/<int:id>/', views.bank_edit, name='bank_edit'),
]