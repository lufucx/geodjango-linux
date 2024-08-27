from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

# Modelo representando temas de conflitos ambientais
class Tema(models.Model):
    nome = models.CharField('Tema', max_length=255, help_text="Especifique o tema do Conflito Ambiental")
    
    class Meta:
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.nome

# Modelo representando os municípios atingidos
class Municipio(models.Model):
    nome = models.CharField('Município Atingido', max_length=255, help_text="Digite o município atingido")

    class Meta:
        verbose_name_plural = 'Municípios Atingidos'

    def __str__(self):
        return self.nome

# Modelo representando os atores envolvidos
class Ator(models.Model):
    nome = models.CharField('Atores envolvidos', max_length=255, help_text="Digite os atores envolvidos")
    
    class Meta:
        verbose_name_plural = 'Atores envolvidos'

    def __str__(self):
        return self.nome

# Modelo representando as populações atingidas
class Populacao(models.Model):
    nome = models.CharField('Populações atingidas', max_length=255, help_text="Especifique a população atingida")

    class Meta:
        verbose_name_plural = 'Populações Atingidas'

    def __str__(self):
        return self.nome

# Modelo representando uma publicação (Post)
class Post(models.Model):
    titulo = models.CharField(max_length=255, help_text="Escreva um título para a sua publicação")
    autor = models.CharField(max_length=255, help_text="Digite os autores da publicação")
    data_publicacao = models.DateTimeField(auto_now_add=True)
    atualizacao_publicacao = models.DateTimeField(auto_now=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    municipio_atingido = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    atores_envolvidos = models.ForeignKey(Ator, on_delete=models.CASCADE)
    populacao_atingida = models.ForeignKey(Populacao, on_delete=models.CASCADE)
    conteudo = CKEditor5Field('Conteúdo', config_name='extends')  # Campo de texto rico usando CKEditor
    fontes = CKEditor5Field('Fontes', config_name='extends')  # Outro campo de texto rico para fontes

    class Meta:
        verbose_name_plural = 'Publicações'

    def __str__(self):
        # Função para exibir o título e autor truncados, se necessário
        max_titulo_length = 50  # Defina o comprimento máximo desejado para o título
        max_autor_length = 50   # Defina o comprimento máximo desejado para o autor

        # Limitando o título
        titulo_str = (self.titulo[:max_titulo_length] + '...') if len(self.titulo) > max_titulo_length else self.titulo

        # Limitando o autor
        autor_str = (self.autor[:max_autor_length] + '...') if len(self.autor) > max_autor_length else self.autor

        return titulo_str + ' | ' + autor_str

    # Funções para formatar datas de publicação e atualização
    def data_publicacao_formatada(self):
        return self.data_publicacao.strftime('%d/%m/%Y')
    
    def data_atualizacao_formatada(self):
        return self.atualizacao_publicacao.strftime('%d/%m/%Y')
