#import string
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect



from django.core import serializers

from django.http import HttpResponse, HttpResponseRedirect

# from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, Client, Order, Tailor, Fabric, Style, SizeTable

from suave.forms import UserForm, ClientRegisterForm, OrderForm, UserFormLogin, TailorRegisterForm

from suave.helper import *

""" 
	@Todo
	>>>>>>>>>>>>>>>>>>>>>>>
	Change Size to have foreign key of Order so we can delete it along with Order-> Client-> and User
	>>>>>>>>>>>>>>>>>>>>>>>

	@Todo
	add estimated time of delivery after order is started


	@Todo
	Have option where users can use their previous/personal measurement

	@Todo
	Make email field in User model unique that is test for email availability before registering users client or tailor

	@Todo
	Add notes option to order use the details field

	@Todo
	Tailor details view should show only service cost i.e cost that relates to the tailor

	@????
	how do I write a function that will take a variable|value from template and work on it

	@Optimize join tailorRegister and clientRegister into one

	@Todo
	Scrutinize Inches and Sizes model

	@Todo
	Clients should edit their orders up to a certain time

	@Todo
	Write function to check if form feilds of order is valid

	@Todo
	Sex should be radio button that dictates size table display
"""


def index(request):
	"""This shows the client home page by default"""
	# messages.success(request, 'Welcome son')
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
	context['title'] = 'SuaveStitches Nigeria'
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
	context['title'] = 'Create order SuaveStitches Nigeria'
	context['order_form'] = OrderForm()
	context['male_size_table'] = SizeTable.objects.filter(size_value__startswith='Ma')
	context['female_size_table'] = SizeTable.objects.filter(size_value__startswith='Fe')

	context['fabrics'] = Fabric.objects.all() #change to choose for male and female
	context['styles'] = Style.objects.all()

	client = Client.objects.get(user=request.user)


	if request.method == 'POST':
		order_form = OrderForm(request.POST)

		#create list from inputs not in a form
		check_input = ['fabric', 'style', 'size']

		checker = checkInput(request, check_input)

		if order_form.is_valid() and checker == True:
			delivery_option = request.POST.get('delivery_option')

			fabric = Fabric.objects.get(id=request.POST.get('fabric'))

			style = Style.objects.get(id=request.POST.get('style'))

			service_option = request.POST.get('service_option')

			total_cost = totalOrderCost(fabric, style, service_option)

			size_table = request.POST.get('size')


			sex = checkSex(size_table)



			new_size_table = SizeTable.objects.get(size_value=size_table)


			order_form_data = order_form.save(commit=False)
			order_form_data.main_order_id = mainOrderId()
			order_form_data.client = client

			order_form_data.delivery_option = delivery_option
			order_form_data.fabric = fabric
			order_form_data.service_option = service_option
			order_form_data.cost = total_cost
			order_form_data.sex = sex
			order_form_data.sizetable = new_size_table

			order_form_data.save()
			return redirect('suave:clientDashboard')

		else:
			context['order_form'] = order_form
			context['error'] = 'Something went wrong - please fill all required fields'
			context['static_errors'] = str(checker)
			render(request, 'i/client/order.html', context)

	return render(request, 'i/client/order.html', context)


def tailorHome(request):
	context = {}
	# context['form'] = ClientForm()
	context['action'] = '/suave/account/tailor'
	context['title'] = 'Tailor --- SuaveStitches Nigeria'
	context['tailorPage'] = True

	return render(request, 'i/tailor/tailor_home.html', context)



def tailorRegister(request):
	context = {}
	context['title'] = 'Tailor Register --- SuaveStitches Nigeria'
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
	context['title'] = 'Tailor - SuaveStitches Nigeria'
	context['tailorPage'] = True
	orders = Order.objects.filter(status='OPEN')
	context['orders'] = orders

	tailor_obj = Tailor.objects.get(user=request.user)
	context['work'] = len(Order.objects.filter(tailor=tailor_obj, status='IN PROGRESS'))
	return render(request, 'i/tailor/dashboard.html', context)


@login_required
def tailorOrderDetails(request, main_order_id):
	try:
		order = Order.objects.get(main_order_id=main_order_id)
	except Exception, e:
		return HttpResponse('can\'t do that %s' %main_order_id) # write better response

	context = {}
	context['title'] = 'Order details -- SuaveStitches Nigeria'
	context['tailorPage'] = True
	context['order'] = order
	print 'order', order.fabric
	# context['size'] = serializers.serialize("python", Size.objects.filter(id=order.size.id))
	context['size'] = serializers.serialize("python", SizeTable.objects.filter(id=order.sizetable.id))
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
	return redirect('suave:tailorDashboard')

@login_required
def tailorWorkInProgress(request):
	context = {}
	tailor_obj = Tailor.objects.get(user=request.user)
	context['work'] = Order.objects.filter(tailor=tailor_obj, status='IN PROGRESS')

	return render(request, 'i/tailor/work.html', context)


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

