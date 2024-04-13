from django.contrib.gis.db import models
from posts.models import Post

class Category(models.Model):
    category_name = models.CharField('Tipo de conflito', max_length=50, help_text="Especifique o tipo de conflito ambiental")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class City(models.Model):
    name = models.CharField('Cidade', max_length=50, help_text="Especifique a cidade da Região")

    class Meta:
        verbose_name_plural = 'Cities'

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

    def __str__(self):
        return self.name