from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core import serializers


# import ast
from suave.models import User, Client, Order, Tailor, Fabric, Style, SizeTable


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
"""


def index(request):
	# logout(request)

	return render(request, 'i/staff/index.html')


@login_required
def admin_gateway(request):
	# print 'request.user', request.user
	return render(request, 'i/staff/admin_gateway.html')


@login_required
def order_list(request):
	context = {}
	context['orders'] = Order.objects.filter(soft_delete=False)
	return render(request, 'i/staff/order_list.html', context)


@login_required
def order_list_deleted(request):
	context = {}
	context['orders'] = Order.objects.filter(soft_delete=True)
	return render(request, 'i/staff/order_list_deleted.html', context)


@login_required
def order_details(request, order_id):
	try:
		order = Order.objects.get(main_order_id=order_id)
	except Exception, e:
		return HttpResponse('can\'t do that %s' %order_id) # write better response

	context = {}
	context['title'] = 'Order details -- SuaveStitches Nigeria'
	# context['tailorPage'] = True
	context['order'] = order
	# get object of order fabric and style to get the name & image in template
	context['fabric'] = Fabric.objects.get(id=order.fabric)
	context['style'] = Style.objects.get(id=order.style)

	context['size'] = serializers.serialize("python", SizeTable.objects.filter(id=order.sizetable.id))
	return render(request, 'i/staff/staff_order_details.html', context)


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
	context = {}
	context['tailors'] =Tailor.objects.all()

	# print 'tailor.newstate', type(specialty)
	return render(request, 'i/staff/tailor_list.html', context)



@login_required
def tailor_details(request, tailor_id):
	context = {}
	tailor = Tailor.objects.get(id=tailor_id)

	##returns [u'name', u'outlook'] -> a raw string
	## BReak it into the individaul specialties
	specialty = str(tailor.specialty)
	## remove left and right sqaure brackets
	specialty = specialty[:-1]
	specialty = specialty[1:]
	specialty = specialty.split(',')
	print specialty
	endpoint = []
	for i in specialty:
		choice = i.replace('u\'', '')
		choice = choice[:-1]

		endpoint.append(choice)

	tailor.specialty = endpoint
	context['tailor'] = tailor
	return render(request, 'i/staff/tailor_details.html', context)


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