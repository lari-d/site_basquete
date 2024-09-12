from django import forms
from .models import Quadra

class QuadraForm(forms.ModelForm):
    class Meta:
        model = Quadra
        fields = '__all__'