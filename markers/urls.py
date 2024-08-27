from django.urls import path
from markers.views import MarkersMapView

app_name = "markers"

# Definição das URLs para o aplicativo 'markers'
urlpatterns = [
    path("", MarkersMapView.as_view(), name='markersmapview'),
]
