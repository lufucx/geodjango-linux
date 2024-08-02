from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('p/<int:pk>/', views.detalhes_post, name='post-detail')
]
