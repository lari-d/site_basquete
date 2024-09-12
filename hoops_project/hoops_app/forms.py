from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Quadra, Time

class UsuarioForm(UserCreationForm):
    telefone = forms.CharField(max_length=20, required=False)
    endereco = forms.CharField(max_length=255, required=False)
    data_nascimento = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(1900, 2025)))
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('Outro', 'Outro')], required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'telefone', 'endereco', 'data_nascimento', 'genero')

class QuadraForm(forms.ModelForm):
    class Meta:
        model = Quadra
        fields = ['nome', 'localizacao', 'disponibilidade']

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['nome', 'cidade', 'jogadores']