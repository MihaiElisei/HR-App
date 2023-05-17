from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
import datetime

# EMPLOYEE
class EmployeeCreateForm(forms.ModelForm):	
	class Meta:
		model = Employee
		exclude = ['is_blocked', 'is_deleted', 'created', 'updated']
		widgets = {
			'birthday': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'}),
			'startdate': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'}),
			'dateissued': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'})
		}

        
# ADD NEW USER
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

# CREATE EMERGENCY FORM
class EmergencyForm(forms.ModelForm):
	class Meta:
		model = Emergency
		fields = ['employee', 'fullname', 'tel', 'location', 'relationship']

# CREATE FAMILY FORM
class FamilyForm(forms.ModelForm):
	class Meta:
		model = Relationship
		fields = ['employee', 'status', 'spouse', 'occupation', 'tel', 'children', 'nextofkin', 'contact', 'relationship', 'father', 'mother']