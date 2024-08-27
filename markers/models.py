from django.contrib.gis.db import models
from posts.models import Post
from django.utils.translation import gettext_lazy as _

# Modelo para armazenar denúncias
class Denuncia(models.Model):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField()
    motivo = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    mensagem = models.TextField()
    arquivos = models.FileField(upload_to='denuncias/', blank=True, null=True)
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Denúncias'

    def __str__(self):
        return f"Denúncia de {self.nome_completo} - {self.motivo}"

# Modelo para armazenar categorias de conflitos ambientais
class Category(models.Model):
    category_name = models.CharField('Tipo de conflito', max_length=50, help_text="Especifique o tipo de conflito ambiental")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category_name

# Modelo para armazenar cidades da região
class City(models.Model):
    name = models.CharField('Cidade', max_length=50, help_text="Especifique a cidade da Região")

    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.name

# Modelo para armazenar marcadores de conflitos ambientais no mapa
class Marker(models.Model):
    name = models.CharField(max_length=255, help_text="Insira um título para o marcador")
    description = models.TextField(blank=True, null=True, help_text="Insira uma descrição para o marcador")
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, default=1, help_text="Escolha o tipo de conflito ambiental")
    city = models.ForeignKey('City', on_delete=models.CASCADE, default=1, help_text="Escolha a cidade do conflito")
    location = models.PointField()  # Campo de ponto geográfico
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, help_text="Escolha a sua publicação para o marcador")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Definição das opções de cores para os ícones dos marcadores
    ICON_CHOICES = (
        ('red', _('Vermelho')),
        ('blue', _('Azul')),
        ('green', _('Verde')),
        ('yellow', _('Amarelo')),
        ('orange', _('Laranja')),
        ('violet', _('Roxo')),
    )
    icon_choice = models.CharField(
        _('Cor do marcador'),
        max_length=10,
        choices=ICON_CHOICES,
        default='green',
        help_text=_("Escolha a cor do marcador!")
    )

    class Meta:
        verbose_name_plural = 'Marcadores'

    def __str__(self):
        return self.name
