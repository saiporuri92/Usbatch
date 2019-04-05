from django.db import models

# Create your models here.
class ABSmodel(models.Model):
	name = models.CharField(max_length=250)
	class Meta:
		abstract=True

class Airport(ABSmodel):
	#name = models.CharField(max_length=250)
	lat = models.CharField(max_length=250)
	log = models.CharField(max_length=250)

class Customer(ABSmodel):
	#name=models.CharField(max_length=250)
	address=models.TextField(max_length=1000, blank=True, null=True)

class Category(ABSmodel):
	#name=models.CharField(max_length=250)
	pass

class Product(ABSmodel):
	#name = models.CharField(max_length=250)
	cost=models.IntegerField(default=0)
	discount = models.IntegerField(blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)

class Sales(models.Model):
	customer=models.ForeignKey(Customer, on_delete=models.PROTECT)
	description=models.TextField(max_length=1000, blank=True, null=True)
	products = models.ManyToManyField(Product)

    
