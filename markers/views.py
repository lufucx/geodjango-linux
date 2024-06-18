import json
from django.core.serializers import serialize
from django.urls import reverse
from django.views.generic import TemplateView
from markers.models import Marker, Category, City
from django.shortcuts import render
from autores.models import Artigo
from tipografia.models import Conflito
from sobre.models import Sobre


class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch markers data
        markers = Marker.objects.all()

        # Serialize markers to GeoJSON format
        serialized_markers = serialize('geojson', markers, fields=('name', 'description', 'location', 'icon_choice'))

        # Fetch articles data
        artigos = Artigo.objects.all()
        conflitos = Conflito.objects.all()
        sobre = Sobre.objects.all()
        
        # Pass serialized markers and articles data to the template context
        context['markers'] = json.loads(serialized_markers)
        context['artigos'] = artigos
        context['conflitos'] = conflitos
        context['sobre'] = sobre

        return context