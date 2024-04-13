from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    tema = models.CharField(max_length=255)
    municipio_atingido = models.CharField(max_length=255)
    atores_envolvidos = models.CharField(max_length=255)
    populacao_atingida = models.CharField(max_length=255)
    fontes = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)