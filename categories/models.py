from django.db import models
from django.contrib.gis.db import models


class Category(models.Model):
    category_name = models.CharField('Tipo de conflito', max_length=50, help_text="Especifique o tipo de conflito ambiental")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta: 
        verbose_name_plural = 'Cities'
    
    def __str__(self):
        return self.name