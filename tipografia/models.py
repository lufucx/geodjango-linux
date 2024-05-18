from django.db import models

class Conflito(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = 'Editar tipografia'

    def __str__(self):
        return self.tipo
