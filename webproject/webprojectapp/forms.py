from dataclasses import fields
from django import forms

from webprojectapp.models import Apartment

class ApartmentForm(forms.ModelForm):
    ciudad = forms.CharField()
    matricula_inmueble = forms.CharField()
    numero_piso = forms.CharField()
    numero_apartamento = forms.CharField()
    numero_habitaciones = forms.CharField()
    numero_banos = forms.CharField()
    precio_dia = forms.CharField()

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
        