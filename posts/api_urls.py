from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TemaViewSet, MunicipioViewSet, AtorViewSet, PopulacaoViewSet, PostViewSet

# Define the router for DRF viewsets
router = DefaultRouter()
router.register(r'temas', TemaViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'atores', AtorViewSet)
router.register(r'populacoes', PopulacaoViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
