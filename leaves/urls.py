from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_leaves, name='all_leaves'),  
    path('leave/apply/', views.create_leave, name='create_leave'), 
    path('leaves/all/action/<int:id>/', views.leaves_action, name='leaves_action'),
] 