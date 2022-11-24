from django.contrib import admin
from clinicaapp.models import Cita
class Citafiltro(admin.ModelAdmin):
    list_display=("id", "nombre")
    search_fields=("id", "nombre") 
admin.site.register(Cita, Citafiltro)    
# Register your models here.
