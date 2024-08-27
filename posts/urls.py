from django.urls import path
from . import views

app_name = 'posts'

# URL patterns para a aplicação posts
urlpatterns = [
    # Rota para exibir detalhes de um post específico
    path('p/<int:pk>/', views.detalhes_post, name='post-detail')
]
