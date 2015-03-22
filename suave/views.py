from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect#, render_to_response

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, Client, Size, Order, Tailor, Fabric, Style

from suave.forms import UserForm, ClientRegisterForm, MaleSizeForm, FemaleSizeForm, OrderForm, UserFormLogin, TailorRegisterForm

from suave.helper import *
# from django.template import RequestContext
""" 
	@Todo
	Change Size to have foreign key of Order so we can delete it along with Order-> Client-> and User

	@Todo
	save size and order at the same time to 

	@Todo
	add estimated time of delivery after order is started

	@Todo 
	View order by tailor on a different page with

	@Todo
	Change dashboard to account for tailor and client

	@Todo
	Create logic for failure in createOrder view

	@Todo
	Have option where users can use their previous/personal measurement

	@Todo
	Seperate cost of fabric from cost of sewing

	@Todo
	Cost = Service charge (based on the type of service chosen) + type of style chosen + fabric chosen

	@Todo
	Add date to Order model

	@Todo
	Saving should be done at the last minute in the login so that you can avoid saving partial forms 
	TailorRegistration needs to be adjusted because it saves before validating the entire form

	@Todo
	Make email field in User model unique that is test for email availoability before registering users client or tailor
"""


def index(request):
	"""This shows the client home page by default"""

	context = {}
	context['title'] = 'SuaveStitches - All the greates tailors in Nigeria at your service'

	return render(request, 'i/index.html', context)


"""register Client"""
def clientRegister(request):
	context = {}
	context['title'] = 'SuaveStitches - Sign up'

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		client_form = ClientRegisterForm(request.POST)

		if user_form.is_valid() and client_form.is_valid():
			data = user_form.cleaned_data

			user_form_data = user_form.save()
			#hash password with set_password() -> save
			user_form_data.set_password(user_form_data.password)
			user_form_data.save()

			#client_form_data holds other client details like sex || preference...
			client_form_data = client_form.save(commit=False)
			#make the client_form_data aware of its one to one relationship with the User
			client_form_data.user = user_form_data

			# save client along with user object
			client_form_data.save()

			#user is authenticated and login is automatic immediately after registering
			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				login(request, user)

			# use ['new_user_check'] to make registration welcome notice display only once || on registration
			request.session['new_user_check'] = 1
			#redirect to clientDashboard view and its associated 'dashboard' page
			return redirect('suave:clientDashboard')

		else:
			context['user_form'] = user_form
			context['client_form'] = client_form

	else:
		context['user_form'] = UserForm()
		context['client_form'] = ClientRegisterForm()

	return render(request, 'i/client/register.html', context)


@login_required
def clientDashboard(request):
	context = {}
	client = Client.objects.get(user=request.user)

	# if new_user_check is 1 then display welcome message
	if request.session['new_user_check'] == 1:
		context['new_user_check'] = True
		request.session['new_user_check'] = 2

	context['orders'] = Order.objects.filter(client=client)

	return render(request, 'i/client/dashboard.html', context)


@login_required
def createOrder(request):
	context = {}

	context['maleSize_form'] = MaleSizeForm()
	context['femaleSize_form'] = FemaleSizeForm()
	context['order_form'] = OrderForm()
	# context['fabrics'] = Fabric.objects.all() #change to choose for male and female
	# print context['fabrics']
	client = Client.objects.get(user=request.user)


	if request.method == 'POST':
		sex = request.POST.get('sex')
		delivery_option = request.POST.get('delivery_option')
		fabric = Fabric.objects.get(id=request.POST.get('fabric'))
		style = Style.objects.get(id=request.POST.get('style'))
		service_option = request.POST.get('service_option')

		total_cost = totalOrderCost(fabric, style, service_option)

		#DEBUG ----------------
		print 'fabric', fabric.cost
		print 'style', style.cost
		print 'service_option', service_option
		print total_cost
		print delivery_option
		#DEBUG ----------------
		"""
		order page has two different forms and only one can be submitted-> dictated by sex.
		process form according to sex
		and assign the size id to size_id
		"""
		if sex == 'F':
			femaleSize_form = FemaleSizeForm(request.POST)
			if femaleSize_form.is_valid():
				femaleSize_form_data = femaleSize_form.save()
				size_id = femaleSize_form_data.id

			else:
				context['femaleSize_form'] = femaleSize_form


		elif(sex == 'M'):
			maleSize_form = MaleSizeForm(request.POST)
			if maleSize_form.is_valid():
				maleSize_form_data = maleSize_form.save()
				size_id = maleSize_form_data.id

			else:
				context['maleSize_form'] = maleSize_form

		# size is saved in the order table
		size = Size.objects.get(id=size_id)

	#prepare order and save
		order_form = OrderForm(request.POST)
		if order_form.is_valid():
			order_form_data = order_form.save(commit=False)
			order_form_data.main_order_id = mainOrderId()
			order_form_data.client = client
			order_form_data.size = size
			order_form_data.sex = sex
			order_form_data.delivery_option = delivery_option
			order_form_data.service_option = service_option
			order_form_data.cost = total_cost
			order_form_data.save()

			return redirect('suave:clientDashboard')

	return render(request, 'i/client/order.html', context)


def tailorHome(request):
	context = {}
	# context['form'] = ClientForm()
	context['action'] = '/suave/account/tailor'
	context['title'] = 'SuaveStitches - Tailor'
	context['tailorPage'] = True

	return render(request, 'i/tailor/tailor_home.html', context)


def tailorRegister(request):
	context = {}
	context['tailorPage'] = True
	context['user_form'] = UserForm()
	context['tailor_form'] = TailorRegisterForm()

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		tailor_form = TailorRegisterForm(request.POST)

		if user_form.is_valid() and tailor_form.is_valid():

			data = user_form.cleaned_data

			user_form_data = user_form.save()
			#hash password with set_password() -> save
			user_form_data.set_password(user_form_data.password)
			user_form_data.save()

			#tailor_form_data holds other client details like rate || specialty || address...
			tailor_form_data = tailor_form.save(commit=False)
			#make the tailor_form_data aware of its one to one relationship with the User
			tailor_form_data.user = user_form_data

			tailor_form_data.save()

			#user is authenticated and login is automatic immediately after registering
			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				login(request, user)

				return redirect('suave:tailorDashboard')

		#invalid form:: return with errors
		else:
			context['user_form'] = user_form
			context['tailor_form'] = tailor_form

	#request not post instantiate forms
	else:
		context['user_form'] = UserForm()
		context['tailor_form'] = TailorRegisterForm()

	#display 'register' page
	return render(request, 'i/tailor/form.html', context)


@login_required
def tailorDashboard(request):
	context = {}
	context['tailorPage'] = True
	orders = Order.objects.filter(status='OPEN')
	context['orders'] = orders
	return render(request, 'i/tailor/dashboard.html', context)


@login_required
def tailorOrderDetails(request, main_order_id):
	try:
		order = Order.objects.get(main_order_id=main_order_id)
	except Exception, e:
		return HttpResponse('can\'t do that %s' %main_order_id) # write better response

	context = {}
	context['tailorPage'] = True
	context['order'] = order
	return render(request, 'i/tailor/order_details.html', context)


@login_required
def tailorStartOrder(request, main_order_id):
	order = Order.objects.get(main_order_id=main_order_id)
	tailor = Tailor.objects.get(user=request.user)
	# print user
	order.tailor = tailor
	order.status = 'IN PROGRESS'
	order.save()
	print 'yes'


"""
	corresponding url 'signin'
	@use Single login logic for Clients and Tailors
	@logic instantiate a 'client' variable, if it is None -> it means the current user is a tailor 
	@return client dashboard if user is client or Tailor dashboard if user is tailor
"""
def signin(request):
	context = {}
	context['user_login'] = UserFormLogin()

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		# login() requires username and password:: use email to get username before authenticating

		try:
			checkUser = User.objects.get(email=email)
		except Exception, e:
			request.session['error'] = 'Incorrect email'
			return redirect('suave:notLoggedIn')

		user = authenticate(username=checkUser.username, password=password)

		if user is not None:
			login(request, user)

			client = None
			# try to get client or tailor
			try:
				client = Client.objects.get(user=user)
			except Exception, e:
				tailor = Tailor.objects.get(user=user)

			# if client is None means user is a tailor
			if client is None:
				return redirect('suave:tailorDashboard')
			else:
				# instantiate session -> 'new_user_check' so  check won't throw undefined keyError in view::clientDashboard 
				request.session['new_user_check'] = 2
				return redirect('suave:clientDashboard')

		else:
			request.session['error'] = 'Login failed try again'
			return redirect('suave:notLoggedIn')

	#request not post send to home page ::-> used as a last resort
	else:
		return redirect('suave:index')


def signout(request):
	logout(request)
	return redirect('suave:index')


def notLoggedIn(request):
	context = {}

	try:
		if request.session['error'] == None:
			request.session['error'] = 'please log in'
		else:
			context['error'] = request.session['error']
	except Exception, e:
		pass

	return render(request, 'i/common/general_login.html', context)



