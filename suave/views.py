from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, Client, Size, Order, Tailor

from suave.forms import UserForm, ClientRegisterForm, MaleSizeForm, FemaleSizeForm, OrderForm



"""This shows the client home page by default"""
def index(request):
	# logout(request)
	context = {}
	context['title'] = 'SuaveStitches - All the greates tailors in Nigeria at your service'

	return render(request, 'i/index_test.html', context)



def clientRegister(request):
	context = {}
	context['action'] = '/suave/register/'
	context['title'] = 'SuaveStitches - Sign up'

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		other_form = ClientRegisterForm(request.POST)

		if user_form.is_valid() and other_form.is_valid():
			#DEBUG 
			data = user_form.cleaned_data
			print data['username']
			print data['password']
			# save user info
			user_form_data = user_form.save()
			#hash password with set_password() -> save
			user_form_data.set_password(user_form_data.password)
			user_form_data.save()

			#other_data holds other client details like sex preference...
			other_form_data = other_form.save(commit=False)
			other_form_data.user = user_form_data

			# save client extra details
			other_form_data.save()
			

			 #@todo use this to display message that last for some time to welcome new users (jquery)
			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				login(request, user)
				print 'Login worked'
			else:
				print 'Login not work'
			request.session['client_id'] = int(other_form_data.id)
			print 'request.session', request.session['client_id']
			request.session['registered'] = 1
			return redirect('suave:clientDashboard')


		else:
			context['user_form'] = user_form
			context['other_form'] = other_form

			print context['user_form'].errors, context['user_form'].errors
	else:
		context['user_form'] = UserForm()
		context['other_form'] = ClientRegisterForm()

	return render(request, 'i/client/form.html', context)

def test(request):
	# me = Client.objects.get(id=request.session['client_id'])
	me = Client.objects.get(id=59)
	print me.user.username
	print me.user.email
	return HttpResponse('heelllo '+ me.user.username)

@login_required #working
def clientDashboard(request):
	##Test for login

	print 'clientDashboard', request.session['client_id']
	client = Client.objects.get(id=request.session['client_id'])
	context = {}
	if request.session['registered'] == 1:
		context['registered'] = True
		request.session['registered'] = 2


	context['username'] = client.user.username
	context['email'] = client.user.email
	context['sex'] = client.sex
	# return HttpResponse('heelllo '+ client.user.username + ' ' + client.user.email + ' ' +  client.sex)
	return render(request, 'i/client/dashboard.html', context)

def tailorHome(request):
	context = {}
	# context['form'] = ClientForm()
	context['action'] = '/suave/account/tailor'
	context['title'] = 'SuaveStitches - Tailor'
	if request.method == 'POST':
		form = ClientRegisterForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return HttpResponseRedirect('/suave')

		else:
			print context['form'].errors

	else:
		context['form'] = ClientRegisterForm()

	return render(request, 'i/tailor/tailor_home.html', context)

def clientHome(request):
	context = {}
	context['title'] = 'SuaveStitches - Customer'
	context['form'] = ClientForm()
	return render(request, 'i/customer/customer_home.html', context)

def order(request):
	context = {}
	# context['action'] = ''
	context['maleSize_form'] = MaleSizeForm()
	context['femaleSize_form'] = FemaleSizeForm()
	context['order_form'] = OrderForm()
	client = Client.objects.get(id=request.session['client_id'])
	# print client['id']

	if request.method == 'POST':
		sex = request.POST.get('sex')
		delivery_option = request.POST.get('delivery_option')

		print delivery_option

		if sex == 'F':
			femaleSize_form = FemaleSizeForm(request.POST)
			if femaleSize_form.is_valid():
				femaleSize_form_data = femaleSize_form.save()

				size_id = femaleSize_form_data.id

		elif(sex == 'M'):
			maleSize_form = MaleSizeForm(request.POST)
			if maleSize_form.is_valid():
				maleSize_form_data = maleSize_form.save()

				size_id = maleSize_form_data.id
		size = Size.objects.get(id=size_id)

	#save order
		order_form = OrderForm(request.POST)
		if order_form.is_valid():
			order_form_data = order_form.save(commit=False)
			order_form_data.client = client
			order_form_data.size = size
			order_form_data.sex = sex
			order_form_data.delivery_option = delivery_option
			order_form_data.status = 'OPEN'
			order_form_data.save()

	return render(request, 'i/client/order.html', context)