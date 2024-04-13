import json
from django.core.serializers import serialize
from django.urls import reverse
from django.views.generic import TemplateView
from markers.models import Marker, Category, City

class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch markers, categories, and cities data
        markers = Marker.objects.all()


        # Serialize markers, categories, and cities to GeoJSON format
        serialized_markers = serialize('geojson', markers, fields=('name', 'description', 'location'))


        # Pass serialized data to the template context
        context['markers'] = json.loads(serialized_markers)

        return context