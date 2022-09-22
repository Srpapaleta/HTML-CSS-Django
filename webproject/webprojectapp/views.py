from django.http import HttpRequest
from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from webprojectapp.forms import ApartmentForm

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
            messages.error(request, "Usuario o contraseña incorrectos")
    
    return render(request, "auth/login.html")

@login_required(login_url="login")
def logut_user(request):
    logout(request)
    return redirect('login')

class FormApartmentView(HttpRequest):

    @login_required(login_url="login")
    def register_form(request):

        apartment = ApartmentForm()
        
        if request.method == 'POST':
            apartment = ApartmentForm(request.POST)
            
            if apartment.is_valid():
                apartment.save()
                messages.success(request, 'Se registró el apartamento correctamente.')
                return redirect('homepage')
        
        return render(request, "apt-register.html", {"form": apartment})