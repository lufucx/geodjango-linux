from django.contrib import admin
from .models import Autor, Artigo

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    verbose_name_plural = "Alunos - Autores"

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['ano']
    filter_horizontal = ['autores']  # Para uma interface de seleção mais amigável

admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
