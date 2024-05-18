from django.contrib import admin
from .models import Conflito

@admin.register(Conflito)
class ConflitoAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'descricao']
