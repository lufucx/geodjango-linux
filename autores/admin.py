from django.contrib import admin
from .models import Autor, Artigo

# Configuração da interface de administração para o modelo Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome']  # Exibe o campo 'nome' na lista de Autores
    verbose_name_plural = "Alunos - Autores"  # Texto para o nome plural no admin

# Configuração da interface de administração para o modelo Artigo
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['ano']  # Exibe o campo 'ano' na lista de Artigos
    filter_horizontal = ['autores']  # Permite a seleção múltipla de autores de maneira amigável

# Registra os modelos no site de administração do Django com suas configurações
admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
