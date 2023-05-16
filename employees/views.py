from django.shortcuts import render

# Create your views here.


def all_employees(request):
    
    return render(request, 'employees/all_employees.html')