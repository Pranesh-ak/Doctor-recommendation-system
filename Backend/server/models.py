from django.db import models

# Create your models here.
class Details(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email=models.EmailField(max_length=40)
    contact=models.BigIntegerField()
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()


