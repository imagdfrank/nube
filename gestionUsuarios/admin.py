from django.contrib import admin
from gestionUsuarios.models import Usuarios,Diagnostico

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
	list_display=("nombre","contra","direccion","email","tfno")

class DiagnosticoAdmin(admin.ModelAdmin):
	list_display=("diagnostico","fecha")
	list_filter=("fecha",)
	date_hierarchy="fecha"

admin.site.register(Usuarios,UsuariosAdmin)
admin.site.register(Diagnostico,DiagnosticoAdmin)