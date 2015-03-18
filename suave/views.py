from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect#, render_to_response

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from suave.models import User, Client, Size, Order, Tailor

from suave.forms import UserForm, ClientRegisterForm, MaleSizeForm, FemaleSizeForm, OrderForm, UserFormLogin, TailorRegisterForm

# from django.template import RequestContext
""" 
	@Todo
	Change Size to have foreign key of Order so we can delete it along with Order-> Client-> and User
	
	@Todo 
	Client and User login
	user = auth
	try 
		good
	except
		bad

	if user.unique
		tailor
	else
		client
"""






def index(request):
	"""This shows the client home page by default"""

	context = {}
	context['title'] = 'SuaveStitches - All the greates tailors in Nigeria at your service'

	return render(request, 'i/index.html', context)


"""register Client"""
def clientRegister(request):
	context = {}
	context['action'] = '/suave/register/'
	context['title'] = 'SuaveStitches - Sign up'

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		client_form = ClientRegisterForm(request.POST)

		if user_form.is_valid() and client_form.is_valid():
			
			data = user_form.cleaned_data
			#DEBUG ----------------
			print data['username']
			print data['password']
			#DEBUG ----------------

			# save user info
			user_form_data = user_form.save()
			#hash password with set_password() -> save
			user_form_data.set_password(user_form_data.password)
			user_form_data.save()

			#client_data holds other client details like sex || preference...
			client_form_data = client_form.save(commit=False)
			#make the client_form_data aware of its one to one relationship with the User
			client_form_data.user = user_form_data

			# save client along with user object
			client_form_data.save()

			##user is authenticated and login is automatic immediately after registering
			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				login(request, user)
			#DEBUG ----------------
			if user.is_authenticated():
				print 'Login worked'
			else:
				print 'Login not work'
			#DEBUG ----------------

			request.session['client_id'] = int(client_form_data.id)
			#DEBUG ----------------
			print 'request.session', request.session['client_id']
			#DEBUG ----------------
			# use ['registered'] to make registration welcome notice display only once||on registration
			request.session['registered'] = 1
			#redirect to clientDashboard view and its associated 'dashboard' page
			return redirect('suave:clientDashboard')
			# return render_to_response('i/client/dashboard.html', context, context_instance=RequestContext(request))


		#invalid form return with errors
		else:
			context['user_form'] = user_form
			context['client_form'] = client_form
			#DEBUG ----------------
			print context['user_form'].errors, context['user_form'].errors
			#DEBUG ----------------
	#request not post display 'register' page
	else:
		context['user_form'] = UserForm()
		context['client_form'] = ClientRegisterForm()

	return render(request, 'i/client/form.html', context)


def test(request):
	# me = Client.objects.get(id=request.session['client_id'])
	me = Client.objects.get(id=59)
	print me.user.username
	print me.user.email
	return HttpResponse('heelllo '+ me.user.username)


@login_required
def clientDashboard(request):
	##Test for login

	print 'clientDashboard', request.session['client_id']
	client = Client.objects.get(id=request.session['client_id'])
	context = {}
	if request.session['registered'] == 1:
		context['registered'] = True
		request.session['registered'] = 2


	context['user'] = client.user
	context['orders'] = Order.objects.filter(client=client)
	context['sex'] = client.sex
	# print 'request.user.username', request.user.username
	# return HttpResponse('heelllo '+ client.user.username + ' ' + client.user.email + ' ' +  client.sex)
	return render(request, 'i/client/dashboard.html', context)
	# return render_to_response('i/client/dashboard.html', context, context_instance=RequestContext(request))


def tailorHome(request):
	context = {}
	# context['form'] = ClientForm()
	context['action'] = '/suave/account/tailor'
	context['title'] = 'SuaveStitches - Tailor'
	context['tailorPage'] = True

	return render(request, 'i/tailor/tailor_home.html', context)


def clientHome(request):
	context = {}
	context['title'] = 'SuaveStitches - Customer'
	context['form'] = ClientForm()
	return render(request, 'i/customer/customer_home.html', context)


def createOrder(request):
	context = {}

	context['maleSize_form'] = MaleSizeForm()
	context['femaleSize_form'] = FemaleSizeForm()
	context['order_form'] = OrderForm()
	client = Client.objects.get(id=request.session['client_id'])


	if request.method == 'POST':
		sex = request.POST.get('sex')
		delivery_option = request.POST.get('delivery_option')
		#DEBUG ----------------
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
			order_form_data.client = client
			order_form_data.size = size
			order_form_data.sex = sex
			order_form_data.delivery_option = delivery_option
			order_form_data.status = 'OPEN'
			order_form_data.save()

	return render(request, 'i/client/order.html', context)


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
			#DEBUG ----------------
			print data['username']
			print data['password']
			#DEBUG ----------------

			# save user info
			user_form_data = user_form.save()
			#hash password with set_password() -> save
			user_form_data.set_password(user_form_data.password)
			user_form_data.save()

			#client_data holds other client details like sex || preference...
			tailor_form_data = tailor_form.save(commit=False)
			#make the tailor_form_data aware of its one to one relationship with the User
			tailor_form_data.user = user_form_data

			# save client along with user object
			tailor_form_data.save()

			##user is authenticated and login is automatic immediately after registering
			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				login(request, user)
			#DEBUG ----------------
			if user.is_authenticated():
				print 'Login worked'
			else:
				print 'Login not work'
			#DEBUG ----------------

			request.session['client_id'] = int(tailor_form_data.id)
			#DEBUG ----------------
			print 'request.session', request.session['client_id']
			#DEBUG ----------------
			# use ['registered'] to make registration welcome notice display only once||on registration
			request.session['registered'] = 1
			#redirect to clientDashboard view and its associated 'dashboard' page
			return redirect('suave:tailorHome')


		#invalid form return with errors
		else:
			context['user_form'] = user_form
			context['tailor_form'] = tailor_form
			#DEBUG ----------------
			# print context['user_form'].errors, context['user_form'].errors
			#DEBUG ----------------
	#request not post display 'register' page
	else:
		context['user_form'] = UserForm()
		context['tailor_form'] = TailorRegisterForm()


	return render(request, 'i/tailor/form.html', context)


"""login a Client or Tailor"""
def signin(request):
	context = {}
	context['user_login'] = UserFormLogin()

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		# print email
		# print password
		checkUser = User.objects.get(email=email)

		username = checkUser.username
		print username

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			client = Client.objects.get(user=user)
			print 'client', client
			print 'Login worked'
		else:
			print 'Login not work'
			return reverse('suave:index')
		# request.session['client_id']
		request.session['client_id'] = client.id
		request.session['registered'] = 2
		print client.id
		print 'type', type(client)
		return redirect('suave:clientDashboard')


	else:
		return redirect('suave:index')

def signout(request):
	logout(request)
	return redirect('suave:index')

