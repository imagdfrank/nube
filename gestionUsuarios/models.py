from django.db import models

# Create your models here.

class Usuarios(models.Model):
	nombre=models.CharField(max_length=30,unique=True)
	contra=models.CharField(max_length=30)
	direccion=models.CharField(max_length=50)
	email=models.EmailField()
	tfno=models.CharField(max_length=10)

class Diagnostico(models.Model):
	diagnostico=models.CharField(max_length=10)
	fecha=models.DateField()