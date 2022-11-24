from django.urls import path
from clinicaapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.inicio, name="inicio"),
    path('login',views.login, name="login"),
    path('horas_disponibles',views.horas_disponibles, name="horas_disponibles"),
    path('historial',views.historial, name="historial"),
    path('cita',views.cita, name="cita"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)