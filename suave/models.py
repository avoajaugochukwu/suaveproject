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


	def __str__(self):
		return self.user.username



class Tailor(models.Model):
# 	#links UserProfile to django User model
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username


class MaleSize(models.Model):

	client = models.ForeignKey(Client)
	center_back = models.IntegerField(default=0)
	chest = models.IntegerField(default=0)
	inside_leg = models.IntegerField(default=0)
	sleeve = models.IntegerField(default=0)
	waist = models.IntegerField(default=0)


# class FemaleSize(models.Model):
# 	client = models.ForeignKey(Client)
# 	bust = models.IntegerField(default=0)
# 	waist = models.IntegerField(default=0)
# 	hips = models.IntegerField(default=0)
# 	inside_leg = models.IntegerField(default=0)