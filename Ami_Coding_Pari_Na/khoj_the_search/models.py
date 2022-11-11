from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class khojmodel(models.Model):
    u_id = models.IntegerField(blank=True,null=True)
    input_values = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add=True)

#This is the main database model..............

class khojm(models.Model):
    user_id = models.IntegerField()
    input_values = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add=True)

