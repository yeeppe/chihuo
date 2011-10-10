from django import forms
import datetime



class RSVPCreateEventForm(forms.Form):
	title = forms.CharField(max_length=30)
	date = forms.DateField(initial=datetime.date.today)
	num_attendance = forms.IntegerField(help_text='Number of people attending')
	place = forms.CharField(max_length=30)
	description = forms.CharField(widget=forms.Textarea())
	email_notification = forms.EmailField(help_text='A notification email address, please')
	