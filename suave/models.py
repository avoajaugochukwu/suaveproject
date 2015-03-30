from django.db import models

from django.contrib.auth.models import User
##tables that are stared will be reviewed later

class Client(models.Model):
	FEMALE = 'F'
	MALE = 'M'
	SEX_CHOICE = (
		(FEMALE, 'F'),
		(MALE, 'M'),
	)

# 	#links UserProfile to django User model
	user = models.OneToOneField(User)

	address = models.CharField(max_length=200, null=True)

	preference = models.CharField(max_length=40)

	sex = models.CharField(max_length=2, choices=SEX_CHOICE, default=" ")

	# size = models.CharField(max_length=40, null=True)


	def __str__(self):
		return self.user.username



class Tailor(models.Model):
# 	#links UserProfile to django User model
	user = models.OneToOneField(User)
	rate = models.IntegerField(default=0)
	phone_number = models.IntegerField(default=0)
	address = address = models.CharField(max_length=300, null=True)
	specialty = models.CharField(max_length=300, null=True)
	# company_size = models.CharField(max_length=300, null=True)
	# sample_pics = models.CharField(max_length=300, null=True) #image field

	def __str__(self):
		return self.user.username

class Size(models.Model):
	#some how I couldnot get a size entry to be deleted along with its related order 'might casue bloated size table when fulfilled orders are dropped'
	# order = models.ForeignKey(Order)
	client = models.ForeignKey(Client, null=True) # make is optional for repeat clients to enter their measurement for ease
	bust = models.CharField(max_length=7, null=True)
	center_back = models.CharField(max_length=7, null=True)
	chest = models.CharField(max_length=7, null=True)
	inside_leg = models.CharField(max_length=7, null=True)
	hips = models.CharField(max_length=7, null=True)
	sleeve = models.CharField(max_length=7, null=True)
	waist = models.CharField(max_length=7, null=True)

	#waistline -> waist for men having validation issues with using wiast for male and female
	waistline = models.CharField(max_length=7, null=True)

	def __str__(self):
		sizeId = str(self.id)
		return sizeId


class Fabric(models.Model):
	name = models.CharField(max_length=100)
	cost = models.IntegerField(null=True)
	sex = models.CharField(max_length=2, null=True)
	pattern = models.CharField(max_length=150, null=True)

	def __str__(self):
		return ('%s %s' %(self.name, self.cost))


class SizeTable(models.Model):
	size_value = models.CharField(max_length=15)
	collar = models.CharField(max_length=10)
	waist = models.CharField(max_length=10)
	hips = models.CharField(max_length=10)

	def __str__(self):
		return self.size_value


class Order(models.Model):

	client = models.ForeignKey(Client, null=True)
	size = models.ForeignKey(Size, null=True)
	#--sizetable
	sizetable = models.ForeignKey(SizeTable, null=True)
	#sizetable
	tailor = models.ForeignKey(Tailor, null=True)
	fabric = models.ForeignKey(Fabric, null=True) #* change to foreign key with Fabric

	main_order_id = models.CharField(max_length=15, null=True)

	details = models.CharField(max_length=250, null=True) #*
	delivery_option = models.CharField(max_length=100, null=True)
	service_option = models.CharField(max_length=100, null=True)
	sex = models.CharField(max_length=2, default=' ')
	status = models.CharField(max_length=20, default='OPEN') #*
	cost = models.IntegerField(default=0000) # final cost of order
	date = models.DateField(auto_now_add=True)


class Style(models.Model):
	name = models.CharField(max_length=50)
	sex = models.CharField(max_length=3)
	cost = models.IntegerField(default=000)

	def __str__(self):
		return ('%s N%s sex- %s' %( self.name, self.cost, self.sex))

class Inches(models.Model):
	size = models.FloatField(default=0000)
	# def __str__(self):
	# 	size = float(self.size)
	# 	return float(self.size)

	def __str__(self):
		size = str(self.size)
		return size

