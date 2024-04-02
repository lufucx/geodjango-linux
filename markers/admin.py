from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from markers.models import Marker


@admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    list_display = ("name", "description", "location", "hyperlink", "categories", "city")
    search_fields = ("name", "description")