from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def SignIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return render(request, "athletes.html")
    return render(request, "signin.html")
def Athletes(request):
    return render(request, "athletes.html")