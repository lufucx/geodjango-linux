import json
from django.core.serializers import serialize
from django.views.generic import TemplateView
from markers.models import Marker
from categories.models import Category, City

class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch markers, categories, and cities data
        markers = Marker.objects.all()
        categories = Category.objects.all()
        cities = City.objects.all()

        # Serialize markers, categories, and cities to GeoJSON format
        serialized_markers = serialize('geojson', markers, fields=('name', 'description', 'location', 'hyperlink'))
        serialized_categories = serialize('geojson', categories, fields=('category_name',))
        serialized_cities = serialize('geojson', cities, fields=('name',))

        # Pass serialized data to the template context
        context['markers'] = json.loads(serialized_markers)
        context['categories'] = json.loads(serialized_categories)
        context['cities'] = json.loads(serialized_cities)

        return context
