from unittest import loader
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppFamiliares.models import Familiar

# Create your views here.

def familiar(self):
    familiar1 = Familiar(nombreYApellido="Agustin Vanetta",
                         dni="37732203", fechaDeNacimiento="1993-06-06")
    familiar1.save()
    familiar2 = Familiar(nombreYApellido="Luca Vanetta",
                         dni="60789654", fechaDeNacimiento="2022-04-11")
    familiar2.save()

    familiar3 = Familiar(nombreYApellido="Giovanni Vanetta",
                         dni="57353461", fechaDeNacimiento="2019-02-20")
    familiar3.save()

    familiares_list=[familiar1,familiar2,familiar3]
    familiares= {"lista":familiares_list}

    plantilla = loader.get_template("home.html")
    documento = plantilla.render(familiares)

    return HttpResponse(documento)