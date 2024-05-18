from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Editar nome dos Autores'

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    ano = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)

    class Meta:
        verbose_name_plural = 'Editar anos/autores'

    def __str__(self):
        return str(self.ano)
