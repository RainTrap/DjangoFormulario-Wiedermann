from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Suscriptor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()