from rest_framework import routers
from markers.viewsets import MarkerViewSet

# Criação de um roteador padrão para as URLs da API
router = routers.DefaultRouter()

# Registro do ViewSet do Marker no roteador
router.register(r"markers", MarkerViewSet)

# URLs geradas automaticamente pelo roteador
urlpatterns = router.urls
