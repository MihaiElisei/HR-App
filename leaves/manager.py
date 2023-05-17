from django.db import models


class LeaveManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()
    
    def all_leaves(self):
        return super().get_queryset().order_by('-created')

    def all_approved_leaves(self):
        '''
        gets all approved leaves -> Leave.objects.all_approved_leaves()
        '''
        return super().get_queryset().filter(status='approved')

    def all_rejected_leaves(self):
        return super().get_queryset().filter(status='rejected').order_by('-created')