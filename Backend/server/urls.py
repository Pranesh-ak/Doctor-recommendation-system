from django.urls import path
from . import views

urlpatterns = [
    path("signup/",views.signup,name="signpage"),
    path("disp/",views.disp,name="display"),
    path("login/",views.log,name="login"),
    path("register",views.register,name="register")
]
