from django.db import models

class Cita(models.Model):
    fecha=models.CharField(max_length=300)
    comentarios=models.CharField(max_length=300, null=True, blank=True)
    paciente=models.CharField(max_length=30, null=True, blank=True)
    email=models.CharField(max_length=300, null=True, blank=True)
    telefono=models.CharField(max_length=300, null=True, blank=True)
    direccion=models.CharField(max_length=300, null=True, blank=True)
    nombre=models.CharField(max_length=300, null=True, blank=True)
   
# Create your models here.
