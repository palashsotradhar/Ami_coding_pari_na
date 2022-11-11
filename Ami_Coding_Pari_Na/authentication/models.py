from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
class regimodel(models.Model):
    username = models.CharField(max_length = 100,unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)
