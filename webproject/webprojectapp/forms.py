from dataclasses import fields
from django import forms

from webprojectapp.models import Apartment

class ApartmentForm(forms.ModelForm):
    error_messages = {
        "invalid" : "El valor debe ser un número entero"
    }

    direccion = forms.CharField(
        label = "Dirección"
    )
    ciudad = forms.CharField()
    matricula_inmueble = forms.CharField(
        label = "Matrícula del inmueble"
    )
    numero_piso = forms.CharField(
        label = "Número de piso",
        error_messages = error_messages
    )
    numero_apartamento = forms.CharField(
        label = "Número de apartamento",
        error_messages = error_messages
    )
    numero_habitaciones = forms.CharField(
        label = "Número de habitaciones",
        error_messages = error_messages
    )
    numero_banos = forms.CharField(
        label = "Número de baños",
        error_messages = error_messages
    )
    precio_dia = forms.CharField(
        label = "Precio / día",
        error_messages = error_messages
    )

    class Meta:
        model = Apartment
        fields = [
            'direccion',
            'ciudad',
            'matricula_inmueble',
            'numero_piso',
            'numero_apartamento',
            'numero_habitaciones',
            'numero_banos',
            'precio_dia',
        ]
        