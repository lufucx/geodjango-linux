import json
from django.urls import reverse
from django.views.generic import TemplateView
from markers.models import Marker, Category, City
from django.shortcuts import render, redirect
from autores.models import Artigo
from tipografia.models import Conflito
from sobre.models import Sobre
from django.contrib.gis.geos import Point
from .forms import DenunciaForm

# View genérica baseada em Template para exibir o mapa de marcadores
class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Busca todos os marcadores
        markers = Marker.objects.all()

        # Construção manual da estrutura GeoJSON
        features = []
        for marker in markers:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [marker.location.x, marker.location.y],
                },
                "properties": {
                    "id": marker.id,
                    "name": marker.name,
                    "description": marker.description,
                    "categories": marker.categories.category_name,
                    "city": marker.city.name,
                    "icon_choice": marker.icon_choice,
                    "post": marker.post.id if marker.post else None,
                },
            }
            features.append(feature)

        # Criação do GeoJSON completo para os marcadores
        serialized_markers = {
            "type": "FeatureCollection",
            "features": features,
        }

        # Busca de dados adicionais para o contexto
        artigos = Artigo.objects.all()
        conflitos = Conflito.objects.all()
        sobre = Sobre.objects.all()

        # Adiciona os dados ao contexto da template
        context['markers'] = serialized_markers
        context['artigos'] = artigos
        context['conflitos'] = conflitos
        context['sobre'] = sobre
        context['form'] = DenunciaForm()

        return context

    # Método POST para lidar com envio de formulários
    def post(self, request, *args, **kwargs):
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('markers:markersmapview')  # Redireciona após o envio
        return self.get(request, *args, form=form, **kwargs)
