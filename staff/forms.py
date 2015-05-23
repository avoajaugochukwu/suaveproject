from django import forms
# from django.contrib.auth.models import User
from suave.models import Client, Tailor, Order, Fabric, Style, SizeTable
# from django.utils.safestring import *
# from django.utils.html import *


class StyleForm(forms.ModelForm):
	name = forms.CharField(max_length=32, help_text="Name", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alade'}))
	sex = forms.CharField(max_length=40, help_text="Sex", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'F, M'}))
	cost = forms.CharField(max_length=32, help_text="Cost", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'N oeoeo'}))
	pattern = forms.CharField(max_length=32, help_text="Pattern", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alademusa@example.com'}))
	description = forms.CharField(max_length=32, help_text="Description", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alademusa@example.com'}))
	# style_img = forms.ImageField(max_length=32, help_text="Description", required=False, widget=forms.FileInput(attrs={}))
	class Meta:
		model = Style
		fields = ('name', 'sex', 'cost', 'pattern', 'description', 'image_url', 'style_img')