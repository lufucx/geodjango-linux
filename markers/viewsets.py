from rest_framework import viewsets
from rest_framework_gis import filters

from markers.models import Marker
from markers.serializers import MarkerSerializer

# ViewSet de leitura para o modelo Marker, permitindo apenas operações de leitura (GET)
class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    # Campo de filtro de caixa delimitadora (bounding box) para localização geográfica
    bbox_filter_field = "location"
    
    # Backend de filtro para permitir filtragem por caixa delimitadora (bbox)
    filter_backends = (
        filters.InBBoxFilter,
    )
    
    # Queryset padrão que retorna todos os objetos Marker
    queryset = Marker.objects.all()
    
    # Serializador utilizado para representar os dados dos objetos Marker
    serializer_class = MarkerSerializer
