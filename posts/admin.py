from django.contrib import admin
from .models import Post, Tema, Municipio, Ator, Populacao

class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_publicacao', 'tema', 'municipio_atingido', 'atores_envolvidos', 'populacao_atingida']
    list_filter = ['autor', 'data_publicacao', 'tema', 'municipio_atingido', 'atores_envolvidos', 'populacao_atingida']
    search_fields = ['titulo', 'tema__nome', 'municipio_atingido__nome', 'atores_envolvidos__nome', 'populacao_atingida__nome']

admin.site.register(Post, PostAdmin)
admin.site.register(Tema)
admin.site.register(Municipio)
admin.site.register(Ator)
admin.site.register(Populacao)
