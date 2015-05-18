from django.db import models

from django.contrib.auth.models import User

class Client(models.Model):
	FEMALE = 'F'
	MALE = 'M'
	SEX_CHOICE = (
		(FEMALE, 'F'),
		(MALE, 'M'),
	)

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
	phone_number = models.CharField(max_length=13, default=0)
	address = address = models.CharField(max_length=300, null=True)
	specialty = models.CharField(max_length=300, null=True)
	approved = models.BooleanField(default=False)
	# company_size = models.CharField(max_length=300, null=True)
	# sample_pics = models.CharField(max_length=300, null=True) #image field

	def __str__(self):
		return self.user.username


class Fabric(models.Model):
	name = models.CharField(max_length=100)
	cost = models.IntegerField(null=True)
	sex = models.CharField(max_length=2, null=True)
	pattern = models.CharField(max_length=150, null=True)
	image_url = models.CharField(max_length=150)
	description = models.CharField(max_length=200, null=True)
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

	#--sizetable
	sizetable = models.ForeignKey(SizeTable, null=True)
	#sizetable
	tailor = models.ForeignKey(Tailor, null=True)
	fabric = models.CharField(max_length=50, null=True)
	style = models.CharField(max_length=100, null=True)

	main_order_id = models.CharField(max_length=15, null=True)

	details = models.CharField(max_length=250, null=True) #*
	delivery_option = models.CharField(max_length=100, null=True)
	service_option = models.CharField(max_length=100, null=True)
	sex = models.CharField(max_length=2, default=' ')
	status = models.CharField(max_length=20, default='OPEN') #*
	## final cost of order
	cost = models.IntegerField(default=0000)
	date = models.DateField(auto_now_add=True)
	## Change to True on First Delete incase error was made
	soft_delete = models.BooleanField(default=False)


class Style(models.Model):
	name = models.CharField(max_length=50)
	sex = models.CharField(max_length=3)
	cost = models.IntegerField(default=000)
	pattern = models.CharField(max_length=150, null=True)
	image_url = models.CharField(max_length=150)
	description = models.CharField(max_length=200, null=True)
	#manipulat img to give them equal size and make different version before saving
	picture = models.ImageField(upload_to='styles', blank=True)



	def __str__(self):
		return ('%s N%s sex- %s' %( self.name, self.cost, self.sex))