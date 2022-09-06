from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return redirect('homepage')

@login_required(login_url="login")
def home(request):
    return render(request, "home.html")

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Credenciales incorrectas")
    
    return render(request, "auth/login.html")

@login_required(login_url="login")
def logut_user(request):
    logout(request)
    return redirect('login')