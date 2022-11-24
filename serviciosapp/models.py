from email.headerregistry import ContentDispositionHeader
from django.db import models

# Create your models here.

class Servicio(models.Model):
    Titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='serviciosapp')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='servicioapp'
        verbose_name_plural='serviciosapp'
    
    def __str__(self):
        return self.Titulo