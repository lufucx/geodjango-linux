from rest_framework import viewsets, permissions
from .models import Post, Tema, Municipio, Ator, Populacao
from .serializers import PostSerializer, TemaSerializer, MunicipioSerializer, AtorSerializer, PopulacaoSerializer


class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
    permission_classes = [permissions.IsAuthenticated]
class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.IsAuthenticated]

class AtorViewSet(viewsets.ModelViewSet):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer
    permission_classes = [permissions.IsAuthenticated]
class PopulacaoViewSet(viewsets.ModelViewSet):
    queryset = Populacao.objects.all()
    serializer_class = PopulacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
