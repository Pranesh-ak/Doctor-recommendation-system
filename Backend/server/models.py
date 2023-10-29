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

class Doctors(models.Model):
    docid=models.AutoField(primary_key=True,unique=True)
    docname=models.CharField(max_length=40)
    specialisation=models.CharField(max_length=40)
    docemail=models.EmailField(max_length=40)
    password=models.CharField(max_length=25)
    contact=models.BigIntegerField()
    address=models.CharField(max_length=75)

class Appointments(models.Model):
    appid=models.AutoField(primary_key=True,unique=True)
    docid=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    pid=models.ForeignKey(Details,on_delete=models.CASCADE)
    appdate=models.CharField(max_length=8)
    apptime=models.CharField(max_length=5)

