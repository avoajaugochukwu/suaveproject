from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core import serializers


# import ast
from suave.models import User, Client, Order, Tailor, Fabric, Style, SizeTable

from staff.forms import *

from staff.helper import *


# Create your views here.
"""
	@Todo
	order_list page should be paginated

	@Todo
	tailor_list page should be organised by approved

	@Todo
	create something for final delete


	@Todo
	On rejection/approval of tailor send email explaining and emcourage them to try to meet up

	@Todo
	Refactor img upload code

	@Todo
	Create alert message that alerts if changes are made to stye fabric order or tailor

	@Todo
	Sort order by date and client for easy search

	@Todo
	Pattern should be added by admin and is a drop down menu
"""


def index(request):
	context = init_context()
	return render(request, 'i/staff/index.login.html', context)


@login_required
def admin_gateway(request):
	context = init_context()
	return render(request, 'i/staff/admin_gateway.html', context)


@login_required
def order_list(request):
	context = {}
	context['orders'] = Order.objects.filter(soft_delete=False)
	return render(request, 'i/staff/order/order_list.html', context)


@login_required
def order_list_deleted(request):
	context = {}
	context['orders'] = Order.objects.filter(soft_delete=True)
	return render(request, 'i/staff/order/order_list_deleted.html', context)


@login_required
def order_details(request, order_id):
	try:
		order = Order.objects.get(main_order_id=order_id)
	except Exception, e:
		return HttpResponse('can\'t do that %s' %order_id) # write better response


	context = init_context()
	context['order'] = order
	# get object of order fabric and style to get the name & image in template
	context['fabric'] = Fabric.objects.get(id=order.fabric)
	context['style'] = Style.objects.get(id=order.style)

	context['size'] = serializers.serialize("python", SizeTable.objects.filter(id=order.sizetable.id))
	return render(request, 'i/staff/order/order_details.html', context)


@login_required
def order_edit(request, order_id):
	return HttpResponse(order_id)


@login_required
def order_delete(request, order_id):
	order_obj = Order.objects.get(main_order_id=order_id)
	order_obj.soft_delete = True
	order_obj.save()
	return HttpResponse(order_obj)





@login_required
def tailor_list(request):
	context = init_context()
	context['tailors'] =Tailor.objects.all()

	# print 'tailor.newstate', type(specialty)
	return render(request, 'i/staff/tailor/tailor_list.html', context)



@login_required
def tailor_details(request, tailor_id):
	context = init_context()
	tailor = Tailor.objects.get(id=tailor_id)

	##returns [u'name', u'outlook'] -> a raw string
	## Break it into the individaul specialties
	specialty = str(tailor.specialty)
	print
	print specialty
	print 
	## remove left and right sqaure brackets
	specialty = specialty[:-1]
	specialty = specialty[1:]

	specialty = specialty.split(',')

	formatted_endpoint = []
	for i in specialty:
		choice = i.replace('u\'', '')
		choice = choice[:-1]

		formatted_endpoint.append(choice)

	tailor.specialty = formatted_endpoint
	context['tailor'] = tailor
	return render(request, 'i/staff/tailor/tailor_details.html', context)



@login_required
def tailor_approve(request, tailor_id):
	tailor = Tailor.objects.get(id=tailor_id)
	tailor.approved = True
	tailor.save()
	return redirect('staff:tailor_list')



@login_required
def tailor_reject(request, tailor_id):

	tailor = Tailor.objects.get(id=tailor_id)
	tailor.approved = False
	tailor.save()

	return redirect('staff:tailor_list')



@login_required
def style_home(request):
	context = init_context()
	context['styles'] = Style.objects.all();

	return render(request, 'i/staff/style/style_home.html', context)


@login_required
def style_add_form(request):
	context = {}
	context['style_form'] = StyleForm()

	if request.method == 'POST':
		style_form = StyleForm(request.POST)
		#check if picture was set
		if style_form.is_valid():
			style = style_form.save(commit=False)

			if 'style_img' in request.FILES:
				style.style_img = request.FILES['style_img']
				print 'ERERERERRERERERER', request.POST.get('style_img')

			#save UserProfile model instance
			print 'request.FILES,request.FILES', request.FILES
			style.save()
		else:
			print 'ERERERERRERERERER', style_form.errors


	return render(request, 'i/staff/style/style_add_form.html', context)


def style_edit(request, style_id):
	context = {}

	old_values = Style.objects.filter(pk=style_id).values()[0]

	style_obj = get_object_or_404(Style, pk=style_id)


	context['style_form'] = StyleForm(old_values)
	context['style_id'] = style_id


	if request.method == 'POST':
		style_form = StyleForm(request.POST,instance=style_obj)
		#check if image was set
		if style_form.is_valid():
			style = style_form.save(commit=False)

			if 'style_img' in request.FILES:
				## check if input image is similar to the one in the database to avoid uploading another version
				## and uploading with different name
				if request.FILES['style_img'] != style_obj.style_img:
					style.style_img = request.FILES['style_img']

			style.save()

			return redirect('staff:style_home')
		else:
			print 'ERERERERRERERERER', style_form.errors



	return render(request, 'i/staff/style/style_edit_form.html', context)


















def signin(request):
	context = {}

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		# login() requires username and password:: use email to get username before authenticating

		try:
			checkUser = User.objects.get(email=email)
		except Exception, e:
			return HttpResponse('cant find user in DB')

		user = authenticate(username=checkUser.username, password=password)

		if user is not None and user.is_staff:
			login(request, user)

			return redirect('staff:admin_gateway')

		else:
			return HttpResponse('Login failed')

	#request not post send to home page ::-> used as a last resort
	else:
		return HttpResponse('Not post')