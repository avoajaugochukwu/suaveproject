from django import forms
from django.contrib.auth.models import User
from suave.models import Client, Tailor, Order, Fabric, Style, SizeTable
"""
	@Todo
	Code for password verifier in comments

"""

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=32, help_text="Username", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alade'}))
	email = forms.EmailField(max_length=40, help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'alademusa@example.com'}))
	password = forms.CharField(max_length=32, help_text="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	# password above will be changed to 'password1'
	#password2 = forms.CharField(max_length=32, help_text="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	# def clean_pass(self):
	# 	password1 = self.cleaned_data.get("password1", "")
	# 	password2 = self.cleaned_data.get("password2")
	# 	if password1 != password2:
	# 		raise forms.ValidationError("Two password not the same")
	# 	return password2

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserFormLogin(UserForm):
	username = forms.CharField(max_length=32, required=True, widget=forms.HiddenInput(attrs={'class': 'hide'}))

	class Meta:
		model = User
		fields = ('email', 'password')
		exclude = ('username',)


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

	##Hidden field ---------------------------------------------------------

	sex = forms.ChoiceField(choices=SEX_CHOICE,  help_text="Sex", required=True, widget=forms.Select(attrs={'class': 'form-control'}))


	class Meta:
		model = Client
		fields = ('sex',)
		# exclude = ('preference', 'address', 'size')

class OrderForm(forms.ModelForm):
	DELIVERY_OPTION = (
		("OFFICE PICKUP", "Office pickup"),
		("HOME DELIVERY","Home Delivery"),
	)

	SEX_CHOICE = (
		('F', 'Female'),
		('M', 'Male'),
	)


	SERVICE_OPTION = (
		('BASIC', 'BASIC'),
		('PREMIUM', 'PREMIUM'),
	)

	# sex = forms.ChoiceField(choices=SEX_CHOICE, help_text="Sex", required=True, widget=forms.RadioSelect(attrs={'class': '', 'style': 'color:#ff0'}))
	delivery_option = forms.ChoiceField(choices=DELIVERY_OPTION, help_text="Choose Delivery option", required=True, widget=forms.RadioSelect(attrs={'class': 'input-xs'}))
	# style = forms.ModelChoiceField(queryset=Style.objects.all(), help_text="Choose style", widget=forms.Select(attrs={'class': 'form-control input-xs'}))
	service_option = forms.ChoiceField(choices=SERVICE_OPTION, help_text="Service Option", widget=forms.Select(attrs={'class': 'form-control input-xs'}))

	class Meta:
		model = Order
		fields = ('service_option', 'delivery_option')
		exclude = ('style',)


class TailorRegisterForm(forms.ModelForm):
	SPECIALTY_SELECTION = (
		("OFFICE PICKUP", "Office pickup"),
		("HOME DELIVERY","Home Delivery"),
		('F', 'Female'),
		('M', 'Male'),
		('BASIC', 'BASIC'),
		('PREMIUM', 'PREMIUM'),
		)
	address = forms.CharField(max_length=200, help_text="Address", required=False, widget=forms. Textarea (attrs={'class': 'form-control'}))
	phone_number = forms.IntegerField(required=False, help_text="Phone number", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08012345678'}))
	rate = forms.IntegerField(required=False, help_text="Rate (in naira)", widget=forms.TextInput(attrs={'class': 'form-control'}))
	specialty = forms.CharField(max_length=40, help_text="Specialty", required=False, widget=forms. Textarea (attrs={'class': 'form-control', 'placeholder': 'Men\'s wear, Women\'s wear, Children\'s wear'}))
	specialty = forms.MultipleChoiceField(help_text="Specialty", required=False,
	 widget=forms.CheckboxSelectMultiple, choices=SPECIALTY_SELECTION)

	class Meta:
		model = Tailor
		fields = ('rate', 'phone_number', 'specialty', 'address')

