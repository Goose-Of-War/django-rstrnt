from django.db import models

# Create your models here.
class FoodItem(models.Model):
	name = models.CharField(max_length=40, primary_key=True)
	price = models.IntegerField()
	img = models.CharField(max_length=200, null=True)
