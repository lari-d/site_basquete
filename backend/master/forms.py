from django import forms
from .models import AluguelQuadra

class AluguelQuadraForm(forms.ModelForm):
    class Meta:
        model = AluguelQuadra
        fields = ['quadra', 'data', 'hora_inicio', 'hora_fim', 'nome_responsável']

