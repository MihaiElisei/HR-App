from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.


def all_employees(request):
    if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
        return redirect('/')

    dataset = dict()
    departments = Department.objects.all()
    employees = Employee.objects.all()

    # PAGINATION
    query = request.GET.get('search')
    if query:
        employees = employees.filter(
			Q(firstname__icontains=query) |
			Q(lastname__icontains=query)
			)
    paginator = Paginator(employees, 5)  # show 5 employees per page
    page = request.GET.get('page')
    employees_paginated = paginator.get_page(page)

    dataset['employee_list'] = employees_paginated
    dataset['departments'] = departments
    dataset['all_employees'] = Employee.objects.all()
    dataset['title'] = 'All Employees'
    return render(request, 'employees/all_employees.html', dataset)



# CREATE NEW EMPLOYEE
def create_employee(request):
	if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
		return redirect('/')

	if request.method == 'POST':
		form = EmployeeCreateForm(request.POST, request.FILES)
		
		if form.is_valid():
			instance = form.save(commit=False)
			user = request.POST.get('user')
			assigned_user = User.objects.get(id=user)

			instance.user = assigned_user

			instance.title = request.POST.get('title')
			instance.firstname = request.POST.get('firstname')
			instance.lastname = request.POST.get('lastname')
			instance.othername = request.POST.get('othername')
			instance.sex = request.POST.get('sex')
			instance.birthday = request.POST.get('birthday')

			nationality_id = request.POST.get('nationality')
			nationality = Nationality.objects.get(id=nationality_id)
			instance.nationality = nationality

			department_id = request.POST.get('department')
			department = Department.objects.get(id=department_id)
			instance.department = department

			instance.address = request.POST.get('address')
			instance.education = request.POST.get('education')
			instance.lastwork = request.POST.get('lastwork')
			instance.position = request.POST.get('position')
		
			role = request.POST.get('role')
			role_instance = Role.objects.get(id=role)
			instance.role = role_instance

			instance.startdate = request.POST.get('startdate')
			instance.employeetype = request.POST.get('employeetype')
			instance.employeeid = request.POST.get('id')
			instance.dateissued = request.POST.get('dateissued')

			instance.save()
			messages.success(request, 'The Employee was added successfully')
			return redirect('employees')
		else:
			messages.error(request, 'Oppppsss... Something went wrong! Please review your inputs!')
			return redirect('create_employee')
	dataset = dict()
	form = EmployeeCreateForm()
	dataset['form'] = form
	dataset['title'] = 'register employee'
	return render(request, 'employees/add_employee.html', dataset)


# EDIT EMPLOYEE
def employee_edit_data(request, id):
    if not (request.user.is_authenticated and request.user.is_superuser and request.user.is_staff):
        return redirect('/')
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeCreateForm(request.POST or None, request.FILES or None, instance=employee)
        if form.is_valid():
            instance = form.save(commit=False)

            user = request.POST.get('user')
            assigned_user = User.objects.get(id=user)

            instance.user = assigned_user

            instance.title = request.POST.get('title')
            instance.firstname = request.POST.get('firstname')
            instance.lastname = request.POST.get('lastname')
            instance.othername = request.POST.get('othername')
            instance.sex = request.POST.get('sex')
            instance.birthday = request.POST.get('birthday')

            nationality_id = request.POST.get('nationality')
            nationality = Nationality.objects.get(id=nationality_id)
            instance.nationality = nationality

            department_id = request.POST.get('department')
            department = Department.objects.get(id=department_id)
            instance.department = department

            instance.address = request.POST.get('address')
            instance.education = request.POST.get('education')
            instance.lastwork = request.POST.get('lastwork')
            instance.position = request.POST.get('position')

            role = request.POST.get('role')
            role_instance = Role.objects.get(id=role)
            instance.role = role_instance

            instance.startdate = request.POST.get('startdate')
            instance.employeetype = request.POST.get('employeetype')
            instance.employeeid = request.POST.get('employeeid')
            instance.dateissued = request.POST.get('dateissued')

            instance.save()
            messages.success(request, 'The Employee was updated successfully')
            return redirect(reverse('employees'))
        else:
            messages.error(request, 'Oppppsss... Something went wrong! Please review your inputs!')

    dataset = dict()
    form = EmployeeCreateForm(request.POST or None, request.FILES or None, instance=employee)
    dataset['form'] = form
    dataset['title'] = 'edit - {0}'.format(employee.get_full_name)
    return render(request, 'employees/add_employee.html',dataset)


# DELETE EMPLOYEE
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, "Employee Deleted Successfully!")
    return redirect('/employees/')


# -----------------------------USERS
# CREATE NEW USER
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            username = form.cleaned_data.get("username")

            messages.success(request, 'Account created for {0} !!!'.format(username))
            return redirect('all_users')
        else:
            messages.error(request, 'Username or password is invalid. Please Try again!')
            return redirect('create_user')
    
    form = CreateUserForm()
    dataset = dict()
    dataset['form'] = form
    dataset['title'] = 'register users'
    return render(request,'employees/create_user.html', dataset)


# VIEW ALL USERS
def all_users(request):
    employees = Employee.objects.all()

    paginator = Paginator(employees,5)  
    page = request.GET.get('page')
    employees_paginated = paginator.get_page(page)

    return render(request,'employees/all_users.html',{'employees':employees_paginated, 'title':'Users List'})