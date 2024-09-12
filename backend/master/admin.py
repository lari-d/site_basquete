from django.contrib import admin
from .models import Quadra, AluguelQuadra, Local

# Register your models here.

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Quadra)
class QuadraAdmin(admin.ModelAdmin):
    list_display=('local','tipo_quadra')

@admin.register(AluguelQuadra)
class AluguelQuadraAdmin(admin.ModelAdmin):
    list_display=('quadra', 'data', 'hora_inicio', 'hora_fim', 'nome_responsavel')
