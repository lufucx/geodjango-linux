from rest_framework_gis.serializers import GeoFeatureModelSerializer
from markers.models import Marker
from rest_framework import serializers
class MarkerSerializer(GeoFeatureModelSerializer):
    categories = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = Marker
        fields = ['id', 'name', 'categories', 'city', 'description', 'post', 'icon_choice']
        geo_field = "location"
