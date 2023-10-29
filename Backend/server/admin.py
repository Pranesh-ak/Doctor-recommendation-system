from django.contrib import admin
from .models import *
# Register your models here.

class signupadmin(admin.ModelAdmin):
    list_display=("id","fname","lname","username","password","email","contact","zip")

admin.site.register(Details,signupadmin)

class docadmin(admin.ModelAdmin):
    list_display=("docid","docname","specialisation","docemail","password","contact","address")

admin.site.register(Doctors,docadmin)

class Appadmin(admin.ModelAdmin):
    list_display=("appid","docid","pid","appdate","apptime")

admin.site.register(Appointments,Appadmin)