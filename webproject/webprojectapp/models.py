from django.db import models

# Create your models here.

""" SQL Process.
1. Migrate model clasess:
    python3 manage.py makemigrations

2. Create SQL code:
    python3 manage.py sqlmigrate webprojectapp {n_migration}

3. Save tables:
    python3 manage.py migrate
"""

class Apartment(models.Model):

    poolOptions = (
        ('SI', 'SI'),
        ('NO', 'NO'),
    )

    id = models.BigAutoField(primary_key=True)
    matricula_inmueble = models.TextField(unique=True)
    ciudad = models.TextField()
    direccion = models.CharField(max_length=50)
    nombre_unidad_residencial = models.CharField(max_length=250)
    numero_piso = models.IntegerField()
    numero_apartamento = models.IntegerField()
    numero_habitaciones = models.IntegerField()
    numero_banos = models.IntegerField()
    tiene_piscina = models.CharField(
        max_length = 2,
        choices = poolOptions,
        default = poolOptions[1]
    )
    precio_dia = models.TextField()