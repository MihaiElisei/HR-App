from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_leaves, name='all_leaves'),  
    path('leave/apply/', views.create_leave, name='create_leave'), 
    path('leaves/all/action/<int:id>/', views.leaves_action, name='leaves_action'),
    path('leave/approve/<int:id>/', views.approve_leave, name='aprove_leave'),
    path('leave/unapprove/<int:id>/', views.unapprove_leave, name='unapprove_leave'),
    path('leave/reject/<int:id>/', views.reject_leave, name='reject'),
    path('leaves/approved/all/', views.approved_leaves, name='approved_leaves'),
    path('leaves/rejected/all/', views.rejected_leaves, name='rejected_leaves')
] 