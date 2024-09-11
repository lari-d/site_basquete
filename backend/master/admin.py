from django.contrib import admin
from .models import Quadra, Aluguel_Quadra

# Register your models here.

@admin.register(Quadra)
class QuadraAdmin(admin.modelAdmin):
    list_display=('local','tipo_quadra')

@admin.register(Aluguel_Quadra)
class Aluguel_QuadraAdmin(admin.modelAdmin):
    list_display=('quadra', 'data', 'hora_inicio', 'hora_fim', 'nome_responsavel')
