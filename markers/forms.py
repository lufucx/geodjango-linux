# forms.py
from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['nome_completo', 'email', 'motivo', 'cidade', 'bairro', 'mensagem', 'arquivos']
