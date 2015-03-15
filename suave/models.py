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

	def __str__(self):
		return self.user.username

class Size(models.Model):
	client = models.ForeignKey(Client)
	bust = models.IntegerField(default=0)
	center_back = models.IntegerField(default=0)
	chest = models.IntegerField(default=0)
	inside_leg = models.IntegerField(default=0)
	hips = models.IntegerField(default=0)
	sleeve = models.IntegerField(default=0)
	waist = models.IntegerField(default=0)



class Order(models.Model):
	client = models.ForeignKey(Client)
	size = models.ForeignKey(Size, null=True)
	tailor = models.ForeignKey(Tailor, null=True)
	Fabric = models.IntegerField(null=True) #* change to foreign key with Fabric
	details = models.CharField(max_length=250, null=True) #*
	delivery_option = models.CharField(max_length=100, null=True)
	sex = models.CharField(max_length=2, default=' ')
	status = models.CharField(max_length=20, default='') #*
	cost = models.IntegerField(default=0) #*
