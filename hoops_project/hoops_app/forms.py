from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Quadra, Time

class UsuarioForm(UserCreationForm):
    nome = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(max_length=15, required=True)
    altura = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
    posicao = forms.CharField(max_length=50, required=True)
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'telefone', 'altura', 'posicao')

class QuadraForm(forms.ModelForm):
    class Meta:
        model = Quadra
        fields = ['nome', 'localizacao', 'disponibilidade']

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['nome', 'cidade', 'jogadores']