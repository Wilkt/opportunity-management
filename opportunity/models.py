from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    

class Account(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Opportunity(models.Model):
	name = models.CharField(max_length=50)
	amount =  models.IntegerField(default=0)
	stage = models.CharField(max_length=50)
	account = models.ForeignKey(Account,on_delete=models.CASCADE)