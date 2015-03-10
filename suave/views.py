from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, UserProfile, Client

from suave.forms import UserForm, UserProfileForm, ClientRegisterForm

def index(request):
	context_dict = {}
	context_dict['title'] = 'SuaveStitches - All the greates tailors in Nigeria at your service'

	return render(request, 'i/index.html', context_dict)

def signUp(request):
	context_dict = {}
	context_dict['title'] = 'SuaveStitches - Sign up'
	context_dict['user_form'] = UserForm()
	# context_dict['user_profile_form'] = UserProfileForm()
	context_dict['client_register_form'] = ClientRegisterForm()
	return render(request, 'i/signUp.html', context_dict)

def tailorHome(request):
	context_dict = {}
	# context_dict['form'] = ClientForm()
	context_dict['action'] = '/suave/account/tailor'
	context_dict['title'] = 'SuaveStitches - Tailor'
	if request.method == 'POST':
		form = ClientRegisterForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return HttpResponseRedirect('/suave')

		else:
			print context_dict['form'].errors

	else:
		context_dict['form'] = ClientRegisterForm()

	return render(request, 'i/tailor/tailor_home.html', context_dict)

def customerHome(request):
	context_dict = {}
	context_dict['title'] = 'SuaveStitches - Customer'
	context_dict['form'] = ClientForm()
	return render(request, 'i/customer/customer_home.html', context_dict)