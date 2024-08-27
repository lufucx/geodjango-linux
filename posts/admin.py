from django.contrib import admin
from .models import Post, Tema, Municipio, Ator, Populacao

# Configurações para o modelo Post no Django Admin
class PostAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista de posts no admin
    list_display = ['titulo', 'autor', 'data_publicacao', 'tema', 'municipio_atingido', 'atores_envolvidos', 'populacao_atingida']
    # Filtros laterais para facilitar a busca por posts
    list_filter = ['autor', 'data_publicacao', 'tema', 'municipio_atingido', 'atores_envolvidos', 'populacao_atingida']
    # Campos pelos quais a busca será realizada
    search_fields = ['titulo', 'tema__nome', 'municipio_atingido__nome', 'atores_envolvidos__nome', 'populacao_atingida__nome']

# Registro dos modelos no Django Admin
admin.site.register(Post, PostAdmin)
admin.site.register(Tema)
admin.site.register(Municipio)
admin.site.register(Ator)
admin.site.register(Populacao)
