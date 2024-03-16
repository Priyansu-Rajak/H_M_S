from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path("",views.Index,name="Index"),
    path("About",views.About,name="about"),
    path("Patientinfo",views.Patient_View,name="Patient_View"),
    path("Contact",views.Contact,name="Contact"),
    path("Login",views.Login,name="Login"),
]