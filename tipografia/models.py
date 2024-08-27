from django.db import models

# Modelo que representa um conflito tipográfico
class Conflito(models.Model):
    tipo = models.CharField(max_length=100)  # Campo de texto para o tipo de conflito
    descricao = models.TextField()  # Campo de texto para a descrição do conflito

    class Meta:
        verbose_name_plural = 'Editar tipografia'  # Nome pluralizado para o Django Admin

    def __str__(self):
        return self.tipo  # Representação textual do modelo, exibindo o tipo de conflito
