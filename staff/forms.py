from django import forms
# from django.contrib.auth.models import User
from suave.models import Client, Tailor, Order, Fabric, Style, SizeTable

from django.utils.html import *


class StyleForm(forms.ModelForm):
	SEX_CHOICE = (
		('F', 'Female'),
		('M', 'Male'),
	)

	name = forms.CharField(max_length=32, help_text="Name", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alade'}))
	sex = forms.ChoiceField(choices=SEX_CHOICE, help_text="Sex", required=True, widget=forms.RadioSelect(attrs={'class': '', 'style': 'color:#ff0'}))
	cost = forms.CharField(max_length=32, help_text="Cost", required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': format_html("In Naira (" + mark_safe("&#x20A6;") + ")")}))
	pattern = forms.CharField(max_length=32, help_text="Pattern", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Flower Skirk or Plain Trouser'}))
	description = forms.CharField(max_length=32, help_text="Description", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Trendy from Ashanti Ghana'}))
	class Meta:
		model = Style
		fields = ('name', 'sex', 'cost', 'pattern', 'description', 'image_url', 'style_img')