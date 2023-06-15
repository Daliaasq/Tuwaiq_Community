from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from main_app.models import Bootcamp
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse

# Create your views here.
def sign_up(request:HttpRequest):
    msg = None
    bootcamps=Bootcamp.objects.all()
    if request.method == "POST":
            bootcamps=Bootcamp(name=request.POST["name"])
            user = User.objects.create_user( username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"],password=request.POST["password"] )
            user.save()
            bootcamps.save()
            return redirect("main_app:home_page")# redirect (Waiting list) 
       
    return render(request, "accounts/sign_up.html", {"msg" : msg, "bootcamps":bootcamps})


def login_page(request:HttpRequest):
        msg = None
        try:
                if request.method == "POST":
                    user : User = authenticate(request, Email=request.POST["Email"], password=request.POST["Password"])
                    if user:
                        login(request, user)
                        return redirect("main_app:home")
                    else:
                        msg = "Incorrect Credentials"
        except:
            msg = "Please choose another username!"
        return render(request, "accounts/login.html")


      
def profile(request:HttpRequest):
    return render(request,'accounts/profile.html')
  

  
def request_page(request : HttpRequest):
    return render(request, "accounts/request.html")


