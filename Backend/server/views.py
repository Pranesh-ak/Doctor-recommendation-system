from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Details
from django.contrib.auth import logout

def signup(request):
    return render(request,"signup.html")

def disp(request):
    return render(request,"display.html",{
        "users":Details.objects.all()
    })


def log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        creds=Details.objects.filter(username=username,password=password)
        if creds:
            messages.success(request,"USER EXISTS")
            return redirect('/disp')
        else:
            messages.error(request,"user does not exist")
            return HttpResponse("USER DOES NOT EXIST")
    else:
        return render(request,"login.html")

def register(request):
    if request.method=='POST':
        fname=request.POST.get('firstName')
        lname=request.POST.get('lastName')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        zip=request.POST.get('zip')
        print("USERNAME IS "+username+" AND PASSWORD IS "+password)
        user=Details(fname=fname,lname=lname,username=username,password=password,email=email,contact=contact,zip=zip)
        user.save()
        messages.success(request,"Your Account Has Been Created Successfully")
        return redirect("/login")