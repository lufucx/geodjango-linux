from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Tema(models.Model):
    nome = models.CharField('Tema', max_length=255, help_text="Especifique o tema do Conflito Ambiental")
    
    class Meta:
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    nome = models.CharField('Município Atingido', max_length=255, help_text="Digite o município atingido")

    class Meta:
        verbose_name_plural = 'Municípios Atingidos'

    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField('Atores envolvidos', max_length=255, help_text="Digite os atores envolvidos")
    
    class Meta:
        verbose_name_plural = 'Atores envolvidos'

    def __str__(self):
        return self.nome

class Populacao(models.Model):
    nome = models.CharField('Populações atingidas', max_length=255, help_text="Especifique a população atingida")

    class Meta:
        verbose_name_plural = 'Populações Atingidas'

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=255, help_text="Escreva um título para a sua publicação")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    municipio_atingido = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    atores_envolvidos = models.ForeignKey(Ator, on_delete=models.CASCADE)
    populacao_atingida = models.ForeignKey(Populacao, on_delete=models.CASCADE)
    conteudo = RichTextField(blank=True, null=True)
    fontes = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)