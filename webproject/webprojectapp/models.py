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

    stateOptions = (
        ('available', 'Disponible'),
        ('unavailable', 'Ocupado'),
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
    precio_dia = models.TextField()
    estado = models.CharField(
        max_length = 20,
        choices = stateOptions,
        default = 'available'
    )

    def get_all():
        return Apartment.objects.all()

    def get_all_availables():
        return len(Apartment.objects.filter(estado = 'available'))

    def get_all_unavailables():
        return len(Apartment.objects.filter(estado = 'unavailable'))

    def get_by_id(apartament_id):
        apartament = Apartment.objects.filter(id = apartament_id)
        if apartament:
            return apartament
        
        return False

    def update_state(apartament, state):       
        return apartament.update(estado = state)