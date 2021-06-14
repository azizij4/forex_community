from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

'''custome register form'''
class UserRestigerForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


'''user update form'''
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

'''profile picture form'''
class Profile_pic_UpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['profile_pc']


