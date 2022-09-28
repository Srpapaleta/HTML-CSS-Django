from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from webprojectapp.forms import ApartmentForm
from webprojectapp.models import Apartment

# Create your views here.

def main(request):
    return redirect('homepage')

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
def home(request):
    context = {
        'appartments': Apartment.get_all(),
        'availables': Apartment.get_all_availables(),
        'unavailables': Apartment.get_all_unavailables(),
    }
    return render(request, "home.html", context)

@login_required(login_url="login")
def logut_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def detailsApartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    return render(request, 'apt-details.html', {'apartment': apartment})

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

class ApartamentActions(HttpRequest):

    @login_required(login_url="login")
    def updateApartamentState(request, id, state):
        # Validations.
        if state not in ['available', 'unavailable']:
            return JsonResponse({
                "status" : 0,
                "message": "Bad request",
            })

        apartament = Apartment.get_by_id(id)
        if apartament == False:
            return JsonResponse({
                "status" : 0,
                "message": "Apartament was not found",
            })

        # Update state.
        if Apartment.update_state(apartament, state):
            return JsonResponse({
                "status" : 1,
                "message": "Apartament updated successfully",
            })
        else:
            return JsonResponse({
                "status" : 0,
                "message": "Internal Error!",
            })

