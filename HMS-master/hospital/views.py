from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import Patient

# Create your views here.
def About(request):
    return render(request,'about.html')
def Patient_View(request):
    if request.method=="POST":
        pname=request.POST['Pname']
        number=request.POST['Number']
        email=request.POST['email']
        age=request.POST['age']
        fees=request.POST['fees']
        add=request.POST['add']
        treatment=request.POST['treatment']
        gender=request.POST['gender']
        new=Patient(name=pname,mobile=number,email=email,age=age,fees=fees,address=add,treatment=treatment,gender=gender)
        new.save()
        return redirect('/')
        
    return render(request,'patient_info.html')
def Contact(request):
    return render(request,'contact.html')
def Index(request):
    return render(request,'index.html')
def Login(request):
   return render(request,'login.html')

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('Login')
    logout(request)
    return redirect('login')