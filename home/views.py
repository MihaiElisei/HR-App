from django.shortcuts import render
from django.views.decorators.cache import cache_control
# Create your views here.


def index(request):
	if request.user.is_authenticated:
		return render(request, "home/dashboard.html")
	else:
		return render(request, "home/index.html")