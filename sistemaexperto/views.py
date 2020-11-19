# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:37:07 2020

@author: MARTIN
"""
import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from gestionUsuarios import models
from sistemaexperto.forms import FormularioContacto

class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #Primera vista
    
    nombre="Martin"
    apellido="Calva"
    var=open("D:/Users/MARTIN/Desktop/ProyectosI+DII/PROYECTOSDJANGO/sistemaexperto/sistemaexperto/plantillas/miplantilla.html")
    plt=Template(var.read())
    var.close()
    ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido})
    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def despedida(request):
    
    p1=Persona("Martin1","Calva1")
    #var=open("D:/Users/MARTIN/Desktop/ProyectosI+DII/PROYECTOSDJANGO/sistemaexperto/sistemaexperto/plantillas/miplantilla2.html")
    #plt=Template(var.read())
    #var.close()
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido})
    documento=plt.render(ctx)
    
    return HttpResponse(documento)


def fecha(request):
    
    fecha_actual=datetime.datetime.now()
    var="""
    <html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    <html>
    """ % fecha_actual
    return HttpResponse(var)

def calculaedad(request, edad, agno):
    
    periodo=agno-2020
    edadfutura=edad+periodo
    documento="""
    <html>
    <body>
    <h2>
    En el año %s tendras %s años
    </body>
    </html>
    """ % (agno,edadfutura)
    
    return HttpResponse(documento)

def index(request):
    
    return render(request,"index.html")
    
def diabetes(request):

    return render(request,"diabetes.html")

def prediabetes(request):

    return render(request,"prediabetes.html")

def diabetesgestacional(request):

    return render(request,"diabetesgestacional.html")

def diabetestipo1(request):

    return render(request,"diabetestipo1.html")

def diabetestipo2(request):

    return render(request,"diabetestipo2.html")

def iniciarsesion(request):

    return render(request,"iniciarsesion.html")


def buscar(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return render(request,"index.html")
    else:
        error=True
        return render(request,"iniciarsesion.html",{'error':error})

def logout_view(request):
    logout(request)
    return render(request,"iniciarsesion.html")

def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['martin.calvaponce@hotmail.com','blackyogo@gmail.com']
        send_mail(subject,message,email_from,recipient_list)

        return render(request,"gracias.html")
    return render(request,"contacto.html")

def registrarse(request):
    return render(request,"registrarse.html")

def ingresar(request):
    myusername = request.POST['apodo']
    mypassword = request.POST['contra']
    myemail = request.POST['email']
    myname = request.POST['nombre']
    mylastname = request.POST['apellido']
    #if myusername ya esta registrador entonces mandar mensaje de error
    #query=User.objects.get(username=myusername)
    #if query:
    #    registrado=True
    #    return render(request,"registrarse.html",{'registrado':registrado})
    user = User.objects.create_user(myusername,myemail,mypassword)
    user.first_name = myname
    user.last_name = mylastname
    user.save()
    if user:
        return render(request,"exito.html")
    else:
        error=True
        return render(request,"registrarse.html",{'error':error})

def encuesta(request):

    return render(request,"encuesta.html")

def pruebaencuesta(request):
    pregunta1 = request.POST['pregunta1']
    pregunta2 = request.POST['pregunta2']
    pregunta3 = request.POST['pregunta3']
    pregunta4 = request.POST['pregunta4']
    pregunta5 = request.POST['pregunta5']
    pregunta6 = request.POST['pregunta6']
    pregunta7 = request.POST['pregunta7']
    pregunta8 = request.POST['pregunta8']
    pregunta9 = request.POST['pregunta9']
    pregunta10 = request.POST['pregunta10']
    pregunta11 = request.POST['pregunta11']
    pregunta12 = request.POST['pregunta12']
    pregunta13 = request.POST['pregunta13']
    pregunta14 = request.POST['pregunta14']
    pregunta15 = request.POST['pregunta15']
    pregunta16 = request.POST['pregunta16']
    pregunta17 = request.POST['pregunta17']
    pregunta18 = request.POST['pregunta18']
    pregunta19 = request.POST['pregunta19']
    pregunta20 = request.POST['pregunta20']
    pregunta21 = request.POST['pregunta21']
    pregunta22 = request.POST['pregunta22']
    pregunta23 = request.POST['pregunta23']
    pregunta24 = request.POST['pregunta24']
    pregunta25 = request.POST['pregunta25']
    pregunta26 = request.POST['pregunta26']
    pregunta27 = request.POST['pregunta27']
    pregunta28 = request.POST['pregunta28']
    pregunta29 = request.POST['pregunta29']
    pregunta30 = request.POST['pregunta30']

    preguntas="""
    Directo: %s Indirecto: %s Contaminacion: %s Lugar Frio: %s Sedentario: %s Falta Actividad: %s Obesidad: %s
    Falta Sueño: %s Pocas horas: %s Alimentacion: %s Estres emocional: %s Ansiedad: %s Medicamentos: %s
    Antidepresivos: %s Tension nerviosa: %s Colesterol: %s Fuma: %s Alcohol: %s Azucar: %s Agua: %s Sed: %s
    Hambre: %s Pierde Peso: %s Orina: %s Vision Borrosa: %s Cansancio: %s Fatiga: %s Entumecen Pies: %s
    Piel Oscurecida: %s Heridas No Cicatrizan: %s
    """%(pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10,
        pregunta11,pregunta12,pregunta13,pregunta14,pregunta15,pregunta16,pregunta17,pregunta18,pregunta19,
        pregunta20,pregunta21,pregunta22,pregunta23,pregunta24,pregunta25,pregunta26,pregunta27,pregunta28,
        pregunta29,pregunta30)
    pon=0
    if pregunta1 == "si":
        pon=pon+8
    if pregunta2 == "si":
        pon=pon+4
    if pregunta3 == "si":
        pon=pon+2
    if pregunta4 == "si":
        pon=pon+1
    if pregunta5 == "si":
        pon=pon+8
    if pregunta6 == "si":
        pon=pon+8
    if pregunta7 == "si":
        pon=pon+10
    if pregunta8 == "si":
        pon=pon+7
    if pregunta9 == "si":
        pon=pon+7
    if pregunta10 == "si":
        pon=pon+9
    if pregunta11 == "si":
        pon=pon+6
    if pregunta12 == "si":
        pon=pon+6
    if pregunta13 == "si":
        pon=pon+8
    if pregunta14 == "si":
        pon=pon+4
    if pregunta15 == "si":
        pon=pon+7
    if pregunta16 == "si":
        pon=pon+7
    if pregunta17 == "si":
        pon=pon+7
    if pregunta18 == "si":
        pon=pon+8
    if pregunta19 == "si":
        pon=pon+3
    if pregunta20 == "si":
        pon=pon+7
    if pregunta21 == "si":
        pon=pon+8
    if pregunta22 == "si":
        pon=pon+7
    if pregunta23 == "si":
        pon=pon+8
    if pregunta24 == "si":
        pon=pon+6
    if pregunta25 == "si":
        pon=pon+9
    if pregunta26 == "si":
        pon=pon+5
    if pregunta27 == "si":
        pon=pon+5
    if pregunta28 == "si":
        pon=pon+8
    if pregunta29 == "si":
        pon=pon+9
    if pregunta30 == "si":
        pon=pon+6
    
    diagnostico=""

    if pon>=0 and pon<60:
        #diagnostico="Riesgo muy bajo de diabetes"
        diagnostico=0
    if pon>=60 and pon <120:
        #diagnostico="Riesgo bajo de diabetes"
        diagnostico=1
    if pon>=120 and pon<=198:
        #diagnostico="Riesgo alto de diabetes"
        diagnostico=2

    #preguntas="""
    #Directo: %s Indirecto: %s Contaminacion: %s Lugar Frio: %s Sedentario: %s Falta Actividad: %s Obesidad: %s
    #Falta Sueño: %s Pocas horas: %s Alimentacion: %s Estres emocional: %s Ansiedad: %s Medicamentos: %s
    #Antidepresivos: %s Tension nerviosa: %s Colesterol: %s Fuma: %s Alcohol: %s Azucar: %s Agua: %s Sed: %s
    #Hambre: %s Pierde Peso: %s Orina: %s Vision Borrosa: %s Cansancio: %s Fatiga: %s Entumecen Pies: %s
    #Piel Oscurecida: %s Heridas No Cicatrizan: %s Ponderacion: %s, Riesgo: %s
    #"""%(pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10,
    #    pregunta11,pregunta12,pregunta13,pregunta14,pregunta15,pregunta16,pregunta17,pregunta18,pregunta19,
    #    pregunta20,pregunta21,pregunta22,pregunta23,pregunta24,pregunta25,pregunta26,pregunta27,pregunta28,
    #    pregunta29,pregunta30,pon,diagnostico)

    #return HttpResponse(preguntas)
    return render(request,"resultado.html",{'diagnostico':diagnostico})