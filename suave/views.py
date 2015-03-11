from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, Client #UserProfile

from suave.forms import UserForm, ClientRegisterForm, MaleSizeForm #UserProfileForm,

"""This shows the client home page by default"""
def index(request):

	context_dict = {}
	context_dict['title'] = 'SuaveStitches - All the greates tailors in Nigeria at your service'

	return render(request, 'i/index.html', context_dict)

def clientRegister(request):
	#boolean for inform template about whether registration was successful


	context_dict = {}
	context_dict['action'] = '/suave/register/'
	context_dict['title'] = 'SuaveStitches - Sign up'
	context_dict['registered'] = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		other_form = ClientRegisterForm(request.POST)

		if user_form.is_valid() and other_form.is_valid():
			# save user info			
			data = user_form.cleaned_data
			print data['username']
			user = user_form.save()
			print user_form.username

			#hash password with set_password() -> save
			user.set_password(user.password)
			user.save()

			#other_data holds other client details like sex preference...
			other_data = other_form.save(commit=False)
			other_data.user = user
			print other_data

			# save client extra details
			other_data.save()

			context_dict['registered'] = True
		else:
			print user_form.errors, other_form.errors
	else:
		context_dict['user_form'] = UserForm()
		context_dict['other_form'] = ClientRegisterForm()

	return render(request, 'i/client/client_form.html', context_dict)


	context_dict['user_form'] = UserForm()
	# context_dict['user_profile_form'] = UserProfileForm()
	context_dict['other_form'] = ClientRegisterForm()


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

def clientHome(request):
	context_dict = {}
	context_dict['title'] = 'SuaveStitches - Customer'
	context_dict['form'] = ClientForm()
	return render(request, 'i/customer/customer_home.html', context_dict)

def sizes(request):
	context_dict = {}
	context_dict['form'] = MaleSizeForm()
	return render(request, 'i/common/sizes.html', context_dict)