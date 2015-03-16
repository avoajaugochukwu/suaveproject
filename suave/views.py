from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, Client, Size, Order, Tailor #UserProfile

from suave.forms import UserForm, ClientRegisterForm, MaleSizeForm, FemaleSizeForm, OrderForm
""" c_d represents context_dict: Used to reduce clutter"""



"""This shows the client home page by default"""
# @login_required
def index(request):
	# logout(request)
	c_d = {}
	c_d['title'] = 'SuaveStitches - All the greates tailors in Nigeria at your service'

	return render(request, 'i/index.html', c_d)

def clientRegister(request):
	c_d = {}
	c_d['action'] = '/suave/register/'
	c_d['title'] = 'SuaveStitches - Sign up'

	#boolean for inform template about whether registration was successful
	c_d['registered'] = False

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
			c_d['user_form'] = user_form
			c_d['other_form'] = other_form

			print c_d['user_form'].errors, c_d['user_form'].errors
	else:
		c_d['user_form'] = UserForm()
		c_d['other_form'] = ClientRegisterForm()

	return render(request, 'i/client/form.html', c_d)

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
	c_d = {}
	if request.session['registered'] == 1:
		c_d['registered'] = True
		request.session['registered'] = 2


	c_d['username'] = client.user.username
	c_d['email'] = client.user.email
	c_d['sex'] = client.sex
	# return HttpResponse('heelllo '+ client.user.username + ' ' + client.user.email + ' ' +  client.sex)
	return render(request, 'i/client/dashboard.html', c_d)

def tailorHome(request):
	c_d = {}
	# c_d['form'] = ClientForm()
	c_d['action'] = '/suave/account/tailor'
	c_d['title'] = 'SuaveStitches - Tailor'
	if request.method == 'POST':
		form = ClientRegisterForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return HttpResponseRedirect('/suave')

		else:
			print c_d['form'].errors

	else:
		c_d['form'] = ClientRegisterForm()

	return render(request, 'i/tailor/tailor_home.html', c_d)

def clientHome(request):
	c_d = {}
	c_d['title'] = 'SuaveStitches - Customer'
	c_d['form'] = ClientForm()
	return render(request, 'i/customer/customer_home.html', c_d)

def order(request):
	c_d = {}
	# c_d['action'] = ''
	c_d['maleSize_form'] = MaleSizeForm()
	c_d['femaleSize_form'] = FemaleSizeForm()
	c_d['order_form'] = OrderForm()
	client = Client.objects.get(id=request.session['client_id'])
	# print client['id']

	if request.method == 'POST':
		sex = request.POST.get('sex')
		delivery_option = request.POST.get('delivery_option')
		# size_id = 1
		print delivery_option
		if sex == 'F':
			femaleSize_form = FemaleSizeForm(request.POST)
			if femaleSize_form.is_valid():
				femaleSize_form_data = femaleSize_form.save()
				print femaleSize_form_data.id
				size_id = femaleSize_form_data.id

		elif(sex == 'M'):
			maleSize_form = MaleSizeForm(request.POST)
			if maleSize_form.is_valid():
				maleSize_form_data = maleSize_form.save()
				print maleSize_form_data.id
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

	return render(request, 'i/client/order.html', c_d)