from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 

def index(request):
    return render (request,"index.html")

def registration(request):
    if request.method== 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1") 
        password2 = request.POST.get("password2")
        
        if password1!=password2 :
            return redirect("registration")
        else :
            my_user=User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect ("log_in")

    return render (request,"registration.html")

def log_in(request):

    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")

        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else :
            return redirect("registration")
       
    return render (request,"login.html" )

def home(request):
    return render(request,"home.html")

def log_out(request):
    logout(request)
    return redirect("index")


