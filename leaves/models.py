from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .manager import *
# Create your models here.


# LEAVE MODEL
class Leave(models.Model):

    SICK = 'sick'
    ANUAL = 'anual'
    EMERGENCY = 'emergency'
    STUDY = 'study'

    LEAVE_TYPE = (
    (SICK,'Sick Leave'),
    (ANUAL,'Anual Leave'),
    (EMERGENCY,'Emergency Leave'),
    (STUDY,'Study Leave'),
    )

    DAYS = 25

    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    startdate = models.DateField(verbose_name=_('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
    enddate = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
    leavetype = models.CharField(verbose_name=_('Leave Type'),choices=LEAVE_TYPE,max_length=25,null=True,blank=False)
    reason = models.CharField(verbose_name=_('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)
    defaultdays = models.PositiveIntegerField(verbose_name=_('Leave days per year counter'),default=DAYS,null=True,blank=True)
	
    status = models.CharField(max_length=12,default='pending')
    is_approved = models.BooleanField(default=False) 

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = LeaveManager()

    class Meta:
        verbose_name = _('Leave')
        verbose_name_plural = ('Leaves')
        ordering = ['-created']
    
    def __str__(self):
        return ('{0} - {1}'.format(self.leavetype,self.user))

    @property
    def leave_days(self):
        days_count = ''
        startdate = self.startdate
        enddate = self.enddate
        if startdate > enddate:
            return
        dates = (enddate - startdate)
        return dates.days

    @property
    def leave_approved(self):
        return self.is_approved == True

    @property
    def approve_leave(self):
        if not self.is_approved:
            self.is_approved = True
            self.status = 'approved'
            self.save()
        return 
    
    @property
    def unapprove_leave(self):
        if self.is_approved:
            self.is_approved = False
            self.status = 'pending'
            self.save()
        return

    @property
    def reject_leave(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'rejected'
            self.save()