from django.shortcuts import render
from .models import Artigo

def mapa(request):
    artigos = Artigo.objects.all()
    return render(request, 'markers/map.html', {'artigos': artigos})
