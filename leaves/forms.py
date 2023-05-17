from django import forms
from .models import *


# CREATE LEAVE FORM
class CreateLeave(forms.ModelForm):
	reason = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
	
	class Meta:
		model = Leave
		exclude = ['user', 'defaultdays', 'hrcomments', 'status', 'is_approved', 'updated', 'created']
		widgets = {
			'startdate': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'}),
			'enddate': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetimefield'})

		}

	def clean_enddate(self):
		enddate = self.cleaned_data['enddate']
		startdate = self.cleaned_data['startdate']
		today_date = datetime.date.today()
		if (startdate or enddate) < today_date:
			raise forms.ValidationError("Selected dates are incorrect, please select again")

		elif startdate >= enddate:
			raise forms.ValidationError("Selected dates are wrong")
		return enddate