from django.test import TestCase
from suave.models import Client

from django.contrib.auth.models import User
# Create your tests here.

class HomePageTest(TestCase):
	def test_case(self):
		resp = self.client.get('/suave/')
		self.assertEqual(resp.status_code, 200)

class ClientRegisterTest(TestCase):

	def test_Case(self):
		one = User.objects.create(username="testCase")
		user = Client.objects.create(user=one, sex='F')
		testCase = Client.objects.get(user=user)

		self.assertEqual(testCase.sex, 'F')

	def test_2Case(self):
		one = User.objects.create(username="test2Case")
		user = Client.objects.create(user=one, sex='M')
		testCase = Client.objects.get(user=user)

		self.assertEqual(testCase.sex, 'F')