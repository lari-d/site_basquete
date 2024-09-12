from django.contrib import admin
from .models import Criar_Partida, Quadra, Aluguel_Quadra, Local

# Register your models here

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display=('nome',) #precisa ter a vírgula para ser uma tupla

@admin.register(Criar_Partida)
class Criar_PartidaAdmin(admin.ModelAdmin):
    list_display=('name_jogo', 'local', 'data', 'hora', 'tipo_jogo', 'tipo_quadra', 'sexo_jogadores')

@admin.register(Quadra)
class QuadraAdmin(admin.ModelAdmin):
    list_display=('local','tipo_quadra')

@admin.register(Aluguel_Quadra)
class Aluguel_QuadraAdmin(admin.ModelAdmin):
    list_display=('quadra', 'data', 'hora_inicio', 'hora_fim', 'nome_responsavel')
