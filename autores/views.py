from django.shortcuts import render
from .models import Artigo

# View para renderizar o mapa com todos os artigos
def mapa(request):
    artigos = Artigo.objects.all()  # Busca todos os artigos no banco de dados
    return render(request, 'markers/map.html', {'artigos': artigos})  # Renderiza a página 'map.html' passando os artigos como contexto
