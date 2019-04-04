from django.db import models

# Create your models here.
class Airport(models.Model):
	name = models.CharField(max_length=250)
	lat = models.CharField(max_length=250)
	log = models.CharField(max_length=250)
class Customer(models.Model):
	pass
