from django.contrib import admin
from .models import Criar_Partida, Local

# Register your models here

@admin.register(Local)
class LocalAdmin(admin.modelAdmin):
    list_display=('nome',) #precisa ter a vírgula para ser uma tupla

@admin.register(Criar_Partida)
class Criar_PartidaAdmin(admin.modelAdmin):
    list_display=('nome_jogo', 'local', 'data', 'hora', 'tipo_jogo', 'tipo_quadra', 'sexo_jogadores')

