from django.db import models

# Create your models here.
class Apartament(models.Model):
    city = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
