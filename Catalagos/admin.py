from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(cat_pais)
# admin.site.register(cat_estados)
admin.site.register(cat_municipios)
admin.site.register(cat_asentamientos)
admin.site.register(cat_religiones)
admin.site.register(cat_tipo_asentamientos)
admin.site.register(cat_escolaridades)

@admin.register(cat_estados)
class Estados(admin.ModelAdmin):

    list_display = ['id','nombre','fk_cat_pais']
    list_display_links = ['id']
    list_filter = ['fk_cat_pais']

