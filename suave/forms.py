from django import forms
from django.contrib.auth.models import User
from suave.models import UserProfile, Client, Tailor


class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=32, help_text="Username", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alade'}))
	email = forms.EmailField(max_length=40, help_text="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'alademusa@example.com'}))
	password = forms.CharField(max_length=32, help_text="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile


class ClientRegisterForm(forms.ModelForm):
	FEMALE = 'F'
	MALE = 'M'
	SEX_CHOICE = (
		(FEMALE, 'F'),
		(MALE, 'M'),
	)

	##Hidden field ---------------------------------------------------------
	address = forms.CharField(max_length=200, required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}))

	preference = forms.CharField(max_length=40, required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}))

	size = forms.CharField(max_length=40, required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
	##Hidden field ---------------------------------------------------------

	sex = forms.ChoiceField(choices=SEX_CHOICE,  help_text="Gender", widget=forms.Select(attrs={'class': 'form-control'}))


	class Meta:
		model = Client
		fields = ('sex',)
		# exclude = ('preference', 'address', 'size')