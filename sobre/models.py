from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Modelo que representa o conteúdo da página "Sobre"
class Sobre(models.Model):
    sobre = CKEditor5Field('Sobre', config_name='extends')  # Campo de texto rico usando CKEditor

    class Meta:
        verbose_name_plural = 'Editar o sobre'  # Nome pluralizado no Django Admin
    
    def __str__(self):
        # Exibe uma versão truncada do conteúdo no Django Admin
        return self.sobre[:50] + ('...' if len(self.sobre) > 50 else '')
