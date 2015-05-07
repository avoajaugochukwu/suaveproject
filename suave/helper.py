from random import randint
import datetime
""" Create a unique identifier for orders using 
		2 numbers of the year e.g '15' for 2015
		2 numbers of the month e.3 '03' for march
		and day
		along with random 4 digit number and a T in front

		>>>> T1503202437

"""
#return value if value is 2: months like 10 or 11
#return 0 + value if value is single digit
def lenOf(value):
	value = str(value)
	if len(value) == 2:
		return str(value)
	else:
		return '0' + str(value)


def mainOrderId():
	orderID = ''
	orderID += str(datetime.datetime.today().year)
	orderID = orderID[2:]

	orderID += lenOf(datetime.datetime.today().month)

	orderID += lenOf(datetime.datetime.today().day)

	for i in range(0, 4):
		orderID += str(randint(0, 9))
	orderID = 'T' + orderID

	return orderID


"""
		Sum cost of fabric, style and service charge (made up of choice of service)
"""
def totalOrderCost(fabric, style, service_option):
	fabricCost = fabric.cost
	styleCost = style.cost
	if service_option == 'BASIC':
		service = 1000
	elif service_option == 'PREMIUM':
		service = 2000

	totalCost = fabricCost + styleCost + service
	return totalCost



"""Check sex by cutting the sizetable response"""
def checkSex(word):
	cut = word[:1]
	if cut == 'M':
		return 'M'
	else:
		return 'F'



"""Check if inputs passed in list were supplied was selected"""
def checkInput(request, check_input):
	# fields_dict = {'sizeTable': 'size table', 'fabric': }
	for i in check_input:
		check = request.POST.get(i)
		if check == None:

			return "'" + i + "'" + " field is required"
	# logic only gets here if all fields are provided
	return True



