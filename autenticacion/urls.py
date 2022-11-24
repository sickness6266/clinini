
import re
from django.urls import path
from . views import registro
from . views import cerrar_sesion,logear
urlpatterns = [
    
    
    path('',registro.as_view(), name="Login"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('logear',logear, name="logear"),
    
     

   

    
]

