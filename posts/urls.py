from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import TemaViewSet, MunicipioViewSet, AtorViewSet, PopulacaoViewSet, PostViewSet

app_name = 'posts'

# Define the router for DRF viewsets
router = DefaultRouter()
router.register(r'temas', TemaViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'atores', AtorViewSet)
router.register(r'populacoes', PopulacaoViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    # Traditional Django views
    path('', views.lista_posts, name='lista_posts'),
    path('p/<int:pk>/', views.detalhes_post, name='post-detail'),
    
    # DRF API views
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
