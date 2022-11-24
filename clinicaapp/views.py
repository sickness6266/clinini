from unittest import loader
from webbrowser import get
from django.shortcuts import render, HttpResponse
from clinicaapp.models import Cita

def inicio(request):
    return render(request,"clinicaapp/inicio.html")
    


def login(request):
    return render(request,"clinicaapp/login.html")



def cita(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_addres = request.POST['your-addres']
        your_scheduler = request.POST['your-scheduler']
        your_message = request.POST['your-message']
        ins = Cita(nombre=your_name,fecha=your_scheduler,telefono=your_phone,direccion=your_addres,email=your_email,comentarios=your_message)
        ins.save()
       
        return render(request,"clinicaapp/cita.html", {
                'your_name': your_name,
                'your_phone': your_phone,
                'your_email': your_email,
                'your_addres': your_addres,
                'your_scheduler': your_scheduler,
                'your_message': your_message,
            })
    else:
        return render(request, "clinicaapp/cita.html")
    


def horas_disponibles(request):
    return render(request,"clinicaapp/horas_disponibles.html")

def historial(request):
    return render(request,"clinicaapp/historial.html")

