from django import forms
from django.contrib.auth.models import User
from suave.models import Client, Tailor, Size, Order


class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=32, help_text="Username", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alade'}))
	email = forms.EmailField(max_length=40, help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'alademusa@example.com'}))
	password = forms.CharField(max_length=32, help_text="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


# class UserProfileForm(forms.ModelForm):
# 	fields = ()
# 	class Meta:
# 		model = UserProfile


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

	# size = forms.CharField(max_length=40, required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
	##Hidden field ---------------------------------------------------------

	sex = forms.ChoiceField(choices=SEX_CHOICE,  help_text="Sex", required=True, widget=forms.Select(attrs={'class': 'form-control'}))


	class Meta:
		model = Client
		fields = ('sex',)
		# exclude = ('preference', 'address', 'size')

class MaleSizeForm(forms.ModelForm):
	SIZES = (
		("24", "24"),
		("25", "25"),
		("26", "26"), 
		("27", "27"),
		("28", "28"),
		("29", "29"),
		("30", "30"),
		)
	center_back = forms.ChoiceField(choices=SIZES, help_text="center_back", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	chest = forms.ChoiceField(choices=SIZES, help_text="chest", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	inside_leg = forms.ChoiceField(choices=SIZES, help_text="inside_leg", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	sleeve = forms.ChoiceField(choices=SIZES, help_text="sleeve", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	waist = forms.ChoiceField(choices=SIZES, help_text="waist", required=True, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = Size
		fields = ('center_back', 'chest', 'inside_leg', 'sleeve', 'waist')

class FemaleSizeForm(forms.ModelForm):
	SIZES = (
		("24", "24"),
		("25", "25"),
		("26", "26"), 
		("27", "27"),
		("28", "28"),
		("29", "29"),
		("30", "30"),
	)
	bust = forms.ChoiceField(choices=SIZES, help_text="bust", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	waist = forms.ChoiceField(choices=SIZES, help_text="waist", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	hips = forms.ChoiceField(choices=SIZES, help_text="hips", required=True, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = Size
		fields = ('bust', 'waist', 'hips')

class OrderForm(forms.ModelForm):
	DELIVERY_OPTION = (
		("OFFICE PICKUP", "Office pickup"),
		("HOME DELIVERY","Home Delivery"),
	)

	SEX_CHOICE = (
		('F', 'F'),
		('M', 'M'),
	)
	sex = forms.ChoiceField(choices=SEX_CHOICE,  help_text="Sex", required=True, widget=forms.RadioSelect(attrs={'class': ''}))
	delivery_option = forms.ChoiceField(choices=DELIVERY_OPTION,  help_text="Choose Delivery option", required=True, widget=forms.RadioSelect(attrs={'class': ''}))

	class Meta:
		model = Order
		fields = ('sex', 'delivery_option')