from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Leave
from employees.models import Employee
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.


# ALL LEAVES LIST
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def all_leaves(request):
	leaves = Leave.objects.all_leaves()
	if request.user.is_superuser:
		paginator = Paginator(leaves, 3)
	else:
		paginator = Paginator(leaves, 8)
	page = request.GET.get('page')
	all_leaves = paginator.get_page(page)
	return render(request,'leaves/leaves.html',{'leave_list': all_leaves})


# CREATE LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def create_leave(request):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = CreateLeave(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			instance.save()

			messages.success(request,'Leave Request Sent')
			return redirect('all_leaves')
		else:
			messages.error(request,'Please check your dates')
			return redirect('create_leave')

	dataset = dict()
	form = CreateLeave()
	dataset['form'] = form
	dataset['title'] = 'Apply for Leave'
	return render(request,'leaves/create_leave.html',dataset)


# LEAVE ACTION
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def leaves_action(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')

	leave = get_object_or_404(Leave, id = id)
	employee = Employee.objects.filter(user = leave.user)[0]
	return render(request,'leaves/leave_action.html',{'leave':leave,'employee':employee,'title':'{0}-{1} leave'.format(leave.user.username,leave.status)})


# APROVE LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def approve_leave(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	user = leave.user
	employee = Employee.objects.filter(user = user)
	leave.approve_leave

	messages.success(request,'Leave successfully approved!')
	return redirect('all_leaves')


# UNAPPROVE LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def unapprove_leave(request,id):
	if not (request.user.is_authenticated and request.user.is_superuser):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.unapprove_leave
	messages.success(request,'Leave successfully unapproved!')
	return redirect('leaves_action', id=id)

# REJECT LEAVE
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def reject_leave(request,id):
	dataset = dict()
	leave = get_object_or_404(Leave, id = id)
	leave.reject_leave
	messages.success(request,'Leave is successfully rejected!')
	return redirect('all_leaves')


# ALL APPROVED LEAVES
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def approved_leaves(request):
	if not (request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	leaves = Leave.objects.all_approved_leaves() 

	paginator = Paginator(leaves, 5)
	page = request.GET.get('page')
	leave_list = paginator.get_page(page)

	return render(request,'leaves/approved_leaves.html',{'leave_list':leave_list})


# ALL REJECTED LEAVES
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="/accounts/login/")
def rejected_leaves(request):
	if not (request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	leaves = Leave.objects.all_rejected_leaves() 
	paginator = Paginator(leaves, 5)
	page = request.GET.get('page')
	leave_list = paginator.get_page(page)

	return render(request,'leaves/rejected_leaves.html',{'leave_list':leave_list,'title':'rejected leave list'})