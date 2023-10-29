from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.signup,name="signpage"),
    path("login/",views.log,name="login"),
    path("register",views.register,name="register"),
    path("home/",views.homepage,name="home"),
    path("bookapp/<int:pid>",views.patients,name="bookapp"),
    path("appoint/<int:pid>/<int:did>",views.appointment,name="appoint"),
    path("valid",views.validate,name="valid")
]
