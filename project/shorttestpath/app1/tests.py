from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from app1.models import Airport

# Create your tests here.
class AirportsTest(TestCase):

	@classmethod
	def setUpClass(cls):
		user = User.objects.create_user(username="user1", password="user1")
		t=Token(user=user)
		t.save()
		user_token = t.key
		cls.client = APIClient()
		#cls.client.login(username="user1", password="user1")
		cls.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token)
	@classmethod
	def tearDownClass(cls):
		cls.client.logout()

	def test_airports_create(self):
		resp = self.client.post("http://localhost:8000/airports/",
			data={"name":"vijayawada","lat":"234","log":"45678"})
		self.assertEqual(200,resp.status_code)
		self.assertEqual(Airport.objects.count(),1)
		#self.assertEqual(Airport.objects.get().name,"vijayawada")



