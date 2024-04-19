from django.contrib.gis.db import models
from posts.models import Post
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    category_name = models.CharField('Tipo de conflito', max_length=50, help_text="Especifique o tipo de conflito ambiental")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category_name

class City(models.Model):
    name = models.CharField('Cidade', max_length=50, help_text="Especifique a cidade da Região")

    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.name


class Marker(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    city = models.ForeignKey('City', on_delete=models.CASCADE, default=1)
    location = models.PointField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)  # Ou ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    ICON_CHOICES = (
        ('red', _('Vermelho')),
        ('blue', _('Azul')),
        ('green', _('Verde')),
        ('yellow', _('Amarelo')),
        ('orange', _('Laranja')),
        ('violet', _('Roxo')),
        # Add more choices as needed
    )
    icon_choice = models.CharField(
        _('Icon choice'),
        max_length=10,
        choices=ICON_CHOICES,
        default='green',  # Default icon choice
        help_text=_("Escolha o tipo de marcador!")
    )

    

    class Meta:
        verbose_name_plural = 'Marcadores'

    def __str__(self):
        return self.name