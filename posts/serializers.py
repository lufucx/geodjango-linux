from rest_framework import serializers
from .models import Tema, Municipio, Ator, Populacao, Post

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = '__all__'

class PopulacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Populacao
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
