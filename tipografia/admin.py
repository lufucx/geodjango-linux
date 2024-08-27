from django.contrib import admin
from .models import Conflito

# Registra o modelo Conflito na interface administrativa do Django
@admin.register(Conflito)
class ConflitoAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'descricao']  # Exibe os campos 'tipo' e 'descricao' na lista do Django Admin
