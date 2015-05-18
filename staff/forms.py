# from django import forms
# from django.contrib.auth.models import User
# from suave.models import Client, Tailor, Order, Fabric, Style, SizeTable
# from django.utils.safestring import *
# from django.utils.html import *


# class StyleForm(forms.ModelForm):
# 	username = forms.CharField(max_length=32, help_text="Username", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alade'}))
# 	email = forms.EmailField(max_length=40, help_text="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'alademusa@example.com'}))
# 	password = forms.CharField(max_length=32, help_text="Password", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))