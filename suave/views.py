#import string

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from django.core import serializers

from django.http import HttpResponse, HttpResponseRedirect

# from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, Client, Order, Tailor, Fabric, Style, SizeTable

from suave.forms import UserForm, ClientRegisterForm, OrderForm, UserFormLogin, TailorRegisterForm

from suave.helper import *
#    ,
# _,,)\.~,,._
# (()`  ``)\))),,_
#  |     \ ''((\)))),,_          ____
#  |6`   |   ''((\())) "-.____.-"    `-.-,
#  |    .'\    ''))))'                  \)))
#  |   |   `.     ''                     ((((
#  \, _)     \/                          |))))
#   `'        |                          (((((
#             \                  |       ))))))
#              `|    |           ,\     /((((((
#               |   / `-.______.<  \   |  )))))
#               |   |  /         `. \  \  ((((
#               |  / \ |           `.\  | (((
#               \  | | |             )| |  ))
#                | | | |             || |  '
# 				       | | | |             || |  
# 				       | | | |             || |  

"""
	@Todo
	add estimated time of delivery after order is started


	@Todo
	Have option where users can use their previous/personal measurement

	@Todo
	Make email field in User model unique that is test for email availability before registering users client or tailor

	@Todo
	Tailor details view should show only service cost i.e cost that relates to the tailor

	@????
	how do I write a function that will take a variable|value from template and work on it

	@Optimize join tailorRegister and clientRegister into one

	@Todo
	Sex should be radio button that dictates size table display

	@Todo
	Email blast to client when order is completed

	@Todo
	Create light box for Fabric and Style images

	@Todo
	Build out staff module to include fabric addition have main iage and auxillary iages

	@Todo
	https://www.upwork.com/b/signup/user-type
	use to build male and female parts of order

	@Todo
	Refactor CSS

	@Todo
	Rewrite lightbox plugin to take into account radio button selection

	@Todo
	Clients should be able to update their orders if they have not been started
	if started they will send email to staff to inform the tailors

	@Todo
	Clients should edit their orders up to a certain time

	@Todo
	Send tailor email if order work takes too much time

	@Todo
	Use helper to check if email is unique using .exist()

	@Todo
	Add logic to accomodate staff in the signin module below[[[[[IMPORTANT]]]]]
"""


"""This shows the client home page by default"""
def index(request):
	context = {}
	context['title'] = 'SuaveStitches - All the greates tailors in Nigeria at your service'

	return render(request, 'i/index.html', context)




""" -> register Client,
		-> log them in automatically,
		-> take them to dashboard where they can start making orders

		@var client_form -> for other attributes of a user
		@var new_user_check::session used to create shake effect for only new users
"""
def client_register(request):
	context = {}
	context['title'] = 'SuaveStitches - Sign up'

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		client_form = ClientRegisterForm(request.POST)

		if user_form.is_valid() and client_form.is_valid():
			data = user_form.cleaned_data

			user_form_data = user_form.save()
			#hash password with set_password()
			user_form_data.set_password(user_form_data.password)
			user_form_data.save()

			#client_form_data holds other client details like sex || preference...
			client_form_data = client_form.save(commit=False)
			#make the client_form_data aware of its one to one relationship with the User
			client_form_data.user = user_form_data

			client_form_data.save()


			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				login(request, user)

			request.session['new_user_check'] = 1

			return redirect('suave:client_dashboard')


		else:
			context['user_form'] = user_form
			context['client_form'] = client_form

	else:
		context['user_form'] = UserForm()
		context['client_form'] = ClientRegisterForm()

	return render(request, 'i/client/register.html', context)



""" -> check if client is new
		-> fetch all orders of the client
"""
@login_required
def client_dashboard(request):
	context = {}
	context['title'] = 'SuaveStitches Nigeria'


	#@Todo
	#write better message
	#Access Control
	check_user = get_object_or_404(Client, user=request.user)
	if check_user is None:
		return HttpResponse('<h1>Fuck OFF NO access</h1>')

	# if new_user_check is 1 then display welcome message
	if request.session['new_user_check'] == 1:
		context['new_user_check'] = True
		request.session['new_user_check'] = 2





	context['orders'] = Order.objects.filter(client=Client.objects.get(user=request.user))

	return render(request, 'i/client/dashboard.html', context)


"""	-> uses helper module
		------> checkInput()			:: ensures all fields are filled
 		------> checkSex()				:: checks sex chosen by client
 		------> mainOrderId() 		:: creates unique id for each other || not ideal if order exceeds 5000
 		------> totalOrderCost()  :: calculates the final cost of each order
		-> displays order page
		-> creates order
"""
@login_required
def create_order(request):
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


		input_check = checkInput(request, ['fabric', 'style', 'size'])


		if order_form.is_valid() and input_check == True:
			


			# get objects of Fabric and Style to compute total_cost
			fabric_obj = Fabric.objects.get(id=request.POST.get('fabric'))
			style_obj = Style.objects.get(id=request.POST.get('style'))
			service_option = request.POST.get('service_option')

			total_cost = totalOrderCost(fabric_obj, style_obj, service_option)

			size_table = request.POST.get('size')

			#use table choice to check sex
			sex = checkSex(size_table)

			new_size_table = SizeTable.objects.get(size_value=size_table)

			order_form_data = order_form.save(commit=False)

			order_form_data.main_order_id = mainOrderId()
			order_form_data.client = client

			# order_form_data.delivery_option = request.POST.get('delivery_option')
			order_form_data.fabric = request.POST.get('fabric')

			# order_form_data.service_option = service_option
			order_form_data.cost = total_cost
			order_form_data.sex = sex

			order_form_data.style = request.POST.get('style')
			order_form_data.sizetable = new_size_table

			order_form_data.save()
			return redirect('suave:client_dashboard')

		else:
			context['order_form'] = order_form
			context['error'] = 'Something went wrong - please fill all required fields'
			#should display only when fabric, style or size is false
			if not input_check:
				context['input_errors'] = str(input_check)



	return render(request, 'i/client/order.html', context)


def tailor_home(request):
	context = {}

	context['title'] = 'SuaveStitches -- Tailor home'
	context['tailorPage'] = True

	return render(request, 'i/tailor/tailor_home.html', context)


""" -> register Tailor,
		-> log them in automatically,
		-> take them to tailor dashboard
		@var tailor_form -> for other attributes of a tailor
"""
def tailor_register(request):
	context = {}
	context['title'] = 'SuaveStitches -- Tailor Register'
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

			#tailor_form_data holds other tailor details like rate || specialty || address...
			tailor_form_data = tailor_form.save(commit=False)
			#make the tailor_form_data aware of its one to one relationship with the User
			tailor_form_data.user = user_form_data

			tailor_form_data.save()

			#user is authenticated and login is automatic immediately after registering
			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				login(request, user)

				return redirect('suave:tailor_dashboard')


		else:
			context['user_form'] = user_form
			context['tailor_form'] = tailor_form

	else:
		context['user_form'] = UserForm()
		context['tailor_form'] = TailorRegisterForm()

	return render(request, 'i/tailor/form.html', context)


"""	-> @use allow tailors to select order to work on
		-> check if tailor has been approved
				if false show not_approved page
"""
@login_required
def tailor_dashboard(request):
	if not request.user.tailor.approved:
		return render(request, 'i/tailor/not_approved.html')

	context = {}
	context['title'] = 'Tailor - SuaveStitches Nigeria'
	context['tailorPage'] = True

	#show only orders that are OPEN hence available to work on
	context['orders'] = Order.objects.filter(status='OPEN')

	tailor_obj = Tailor.objects.get(user=request.user)

	#get the number of work in progress of current tailor
	context['work'] = len(Order.objects.filter(tailor=tailor_obj, status='IN PROGRESS'))

	return render(request, 'i/tailor/dashboard.html', context)



""" -> @use Tailor sees all details of order before deciding to work on it
		-> @ add module to inform that this order is taken *********
"""
@login_required
def tailor_order_details(request, main_order_id):

	#check that order is valid
	try:
		order = Order.objects.get(main_order_id=main_order_id)
	except Exception, e:
		return HttpResponse('can\'t do that %s' %main_order_id)

	context = {}
	context['title'] = 'SuaveStitches || Order details'
	context['tailorPage'] = True
	context['order'] = order
	# get object of order fabric and style to get the name & image in template
	context['fabric'] = Fabric.objects.get(id=order.fabric)
	context['style'] = Style.objects.get(id=order.style)

	context['size'] = serializers.serialize("python", SizeTable.objects.filter(id=order.sizetable.id))
	return render(request, 'i/tailor/order_details.html', context)



"""	-> @use mark order as started
		-> @add current tailor name to order and change status to 'IN PROGESS'
"""
@login_required
def tailor_start_order(request, main_order_id):

	order = Order.objects.get(main_order_id=main_order_id)
	tailor = Tailor.objects.get(user=request.user)

	#save tailor name and status in order
	order.tailor = tailor
	order.status = 'IN PROGRESS'
	order.save()

	return redirect('suave:tailor_dashboard')


"""	-> @use show current tailor jobs that are still going on 
"""
@login_required
def tailor_work_in_progress(request):
	context = {}
	context['tailorPage'] = True
	tailor_obj = Tailor.objects.get(user=request.user)
	context['work'] = Order.objects.filter(tailor=tailor_obj, status='IN PROGRESS')

	return render(request, 'i/tailor/work.html', context)


"""	-> @use Single login logic for Clients and Tailors
		-> instantiate a 'client' variable 
				if it is None 
					it means the current user is a tailor 
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
			check_user = User.objects.get(email=email)
		except Exception, e:
			request.session['error'] = 'Incorrect email'
			return redirect('suave:login_failed')

		user = authenticate(username=check_user.username, password=password)

		if user is not None:
			login(request, user)

			client = None
			# try to get client or tailor object
			try:
				client = Client.objects.get(user=user)
			except Exception, e:
				tailor = Tailor.objects.get(user=user)

			# if client is None means user is a tailor
			if client is None:
				return redirect('suave:tailor_dashboard')
			else:
				# set 'new_user_check' to avoid error in view::client_dashboard 
				request.session['new_user_check'] = 2
				return redirect('suave:client_dashboard')

		else:
			request.session['error'] = 'Login failed try again'
			return redirect('suave:login_failed')

	#request not post send to home page ::-> used as a last resort
	else:
		return redirect('suave:index')


def signout(request):
	logout(request)
	return redirect('suave:index')


def login_failed(request):
	context = {}

	try:
		if request.session['error'] == None:
			request.session['error'] = 'please log in'
			context['error'] = request.session['error']
		else:
			context['error'] = request.session['error']
	except Exception, e:
		pass

	return render(request, 'i/common/general_login.html', context)

