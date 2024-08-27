from django.db import models

# Modelo representando um Autor
class Autor(models.Model):
    nome = models.CharField(max_length=100)  # Campo de texto para o nome do autor

    class Meta:
        verbose_name_plural = 'Editar nome dos Autores'  # Texto personalizado para o nome plural

    def __str__(self):
        return self.nome  # Retorna o nome do autor como representação do objeto

# Modelo representando um Artigo
class Artigo(models.Model):
    ano = models.CharField(max_length=100)  # Campo de texto para o ano do artigo
    autores = models.ManyToManyField(Autor)  # Relacionamento muitos-para-muitos com o modelo Autor

    class Meta:
        verbose_name_plural = 'Editar anos/autores'  # Texto personalizado para o nome plural

    def __str__(self):
        return str(self.ano)  # Retorna o ano como representação do objeto