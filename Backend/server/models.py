from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email=models.EmailField(max_length=40)
    contact=models.BigIntegerField()
    zip=models.IntegerField()


