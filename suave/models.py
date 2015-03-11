from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)


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

	size = models.CharField(max_length=40, null=True)





	##
	# User provides firstname lastname username email password
	# firstname = models.CharField(max_length=32)
	# lastname = models.CharField(max_length=32)
	# email = models.EmailField(max_length=100)
	# password = models.CharField(max_length=32)

	def __str__(self):
		return self.user.username



class Tailor(models.Model):
# 	#links UserProfile to django User model
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username