from django import forms
from django.contrib.auth.models import User
from suave.models import Client, Tailor, Size, Order, Fabric, Style, Inches


class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=32, help_text="Username", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alade'}))
	email = forms.EmailField(max_length=40, help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'alademusa@example.com'}))
	password = forms.CharField(max_length=32, help_text="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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

	# size = forms.CharField(max_length=40, required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
	##Hidden field ---------------------------------------------------------

	sex = forms.ChoiceField(choices=SEX_CHOICE,  help_text="Sex", required=True, widget=forms.Select(attrs={'class': 'form-control'}))


	class Meta:
		model = Client
		fields = ('sex',)
		# exclude = ('preference', 'address', 'size')

class MaleSizeForm(forms.ModelForm):
	SIZES = (
		('', '----'),
		("24", "24"),
		("25", "25"),
		("26", "26"), 
		("27", "27"),
		("28", "28"),
		("29", "29"),
		("30", "30"),
		)
	center_back = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), help_text="center_back", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	chest = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), help_text="chest", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	inside_leg = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), help_text="inside_leg", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	sleeve = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), help_text="sleeve", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	waistline = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), help_text="waistline", required=True, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = Size
		fields = ('center_back', 'chest', 'inside_leg', 'sleeve', 'waistline')

class FemaleSizeForm(forms.ModelForm):
	SIZES = (
		('', '----'),
		("24", "24"),
		("25", "25"),
		("26", "26"), 
		("27", "27"),
		("28", "28"),
		("29", "29"),
		("30", "30"),
	)
	bust = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), to_field_name="size", help_text="bust", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	waist = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), to_field_name="size", help_text="waist", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	# hips = forms.ChoiceField(choices=SIZES, help_text="hips", required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	hips = forms.ModelChoiceField(queryset=Inches.objects.filter(size__gt=7.5, size__lt=30), to_field_name="size", required=True, help_text="hips", widget=forms.Select(attrs={'class': 'form-control'}))
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


	SERVICE_OPTION = (
		('BASIC', 'BASIC'),
		('PREMIUM', 'PREMIUM'),
	)

	sex = forms.ChoiceField(choices=SEX_CHOICE, help_text="Sex", required=True, widget=forms.RadioSelect(attrs={'class': ''}))
	delivery_option = forms.ChoiceField(choices=DELIVERY_OPTION, help_text="Choose Delivery option", required=True, widget=forms.RadioSelect(attrs={'class': ''}))
	fabric = forms.ModelChoiceField(queryset=Fabric.objects.all(), help_text="Choose fabric", widget=forms.Select(attrs={'class': 'form-control'}))
	style = forms.ModelChoiceField(queryset=Style.objects.all(), help_text="Choose style", widget=forms.Select(attrs={'class': 'form-control'}))
	service_option = forms.ChoiceField(choices=SERVICE_OPTION, help_text="Service Option", widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = Order
		fields = ('sex', 'delivery_option', 'fabric', 'style')


class TailorRegisterForm(forms.ModelForm):
	address = forms.CharField(max_length=200, help_text="Address", required=False, widget=forms. Textarea (attrs={'class': 'form-control'}))
	phone_number = forms.IntegerField(required=False, help_text="Phone number", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08012345678'}))
	rate = forms.IntegerField(required=False, help_text="Rate (in naira)", widget=forms.TextInput(attrs={'class': 'form-control'}))
	specialty = forms.CharField(max_length=40, help_text="Specialty", required=False, widget=forms. Textarea (attrs={'class': 'form-control', 'placeholder': 'Men\'s wear, Women\'s wear, Children\'s wear'}))

	class Meta:
		model = Tailor
		fields = ('rate', 'phone_number', 'specialty', 'address')