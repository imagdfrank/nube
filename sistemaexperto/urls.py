"""sistemaexperto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import login, logout
from django.config import settings
from django.config.urls.static import static
from sistemaexperto.views import *
from gestionUsuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', saludo),
    path('adios/', despedida),
    path('fecha/', fecha),
    path('edad/<int:edad>/<int:agno>', calculaedad),
    path('',index, name='index'),
    path('diabetes/',diabetes, name='diabetes'),
    path('prediabetes/',prediabetes, name='prediabetes'),
    path('diabetesgestacional/',diabetesgestacional, name='diabetesgestacional'),
    path('diabetestipo1/',diabetestipo1, name='diabetestipo1'),
    path('diabetestipo2/',diabetestipo2, name='diabetestipo2'),
    path('iniciarsesion/',iniciarsesion, name='iniciarsesion'),
    path('buscar/',buscar,name='buscar'),
    path('contacto/',contacto,name='contacto'),
    path('registrarse/',registrarse,name='registrarse'),
    path('salir/',logout_view,name='logout_view'),
    path('ingresar/',ingresar,name='ingresar'),
    path('encuesta/',encuesta,name='encuesta'),
    path('pruebaencuesta/',pruebaencuesta,name='pruebaencuesta'),
    #path('resultado/',resultado,name='resultado'),
]+static(settings.STATIC_URL, document_root=settins.STATIC_ROOT)