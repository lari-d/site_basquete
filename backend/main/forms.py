from django import forms
from .models import Criar_Partida

class PartidaForm(forms.ModelForm):
    class Meta: #fornece metadados ao django
        model = Criar_Partida
        fields = '__all__' #lista de campos que devem ser inseridos no formulário
