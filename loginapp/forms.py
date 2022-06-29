import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import pytz

from loginapp.models import UserLog


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserLogForm(forms.ModelForm):
	class Meta:
		model = UserLog
		fields = ("username","login_time","logout_time","session_time")

	def save(self, commit=True):
		userlog = super(UserLogForm, self).save(commit=False)
		userlog.logout_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
		if commit:
			userlog.save()
		return userlog