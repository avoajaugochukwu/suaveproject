from random import randint
import datetime
""" Create a unique identifier for orders using 
		2 numbers of the year e.g '15' for 2015
		2 numbers of the month e.3 '03' for march
		and day
		along with random 4 digit number and a T in front

		>>>> T1503202437

"""
def mainOrderId():
	orderID = ''
	orderID += str(datetime.datetime.today().year)
	orderID = orderID[2:]
	orderID += '0'
	orderID += str(datetime.datetime.today().month)
	orderID += str(datetime.datetime.today().day)

	for i in range(0, 4):
		orderID += str(randint(0, 9))
	orderID = 'T' + orderID

	return orderID