from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Sobre(models.Model):
    sobre = CKEditor5Field('Sobre', config_name='extends')

    class Meta:
        verbose_name_plural = 'Editar o sobre'
    
    def __str__(self):
        return self.sobre[:50] + ('...' if len(self.sobre) > 50 else '')