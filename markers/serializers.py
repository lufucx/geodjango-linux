from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
)

from markers.models import Marker


class MarkerSerializer(
    GeoFeatureModelSerializer
):
    class Meta:
        fields = ['id', 'name', 'description', 'hyperlink']
        geo_field = "location"
        model = Marker