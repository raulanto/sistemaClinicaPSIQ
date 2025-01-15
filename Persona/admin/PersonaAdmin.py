from django.contrib import admin
from ..models.Persona import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass
