from django.contrib import admin
from .models import *
# Register your models here.

class signupadmin(admin.ModelAdmin):
    list_display=("id","fname","lname","username","password","email","contact","zip")

admin.site.register(Details,signupadmin)

