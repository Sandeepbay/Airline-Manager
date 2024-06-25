from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request , "users/index.html")
    
def login_form(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request , "users/login.html" , {
                "message": "Invalid Details"
            })
        
    return render(request , "users/login.html")

def logout_form(request):
    logout(request)
    return render(request , "users/login.html" , {
        "message": "You have been logged out"
    })