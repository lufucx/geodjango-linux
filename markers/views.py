import json
from django.core.serializers import serialize
from django.views.generic import TemplateView
from markers.models import Marker

class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        markers = Marker.objects.all()
        serialized_markers = serialize('geojson', markers, fields=('name', 'description', 'location', 'hyperlink'))
        context['markers'] = json.loads(serialized_markers)
        return context