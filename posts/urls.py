from django.urls import path
from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('p/<int:pk>/', views.detalhes_post, name='post-detail'),
]
