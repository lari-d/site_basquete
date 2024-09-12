from django.shortcuts import render, redirect 
from django.http import JsonResponse
from .models import Criar_Partida
from .forms import PartidaForm 

# Create your views here.

#Listar uma partida
def listar_partidas(request):
    partidas = Criar_Partida.objects.all() #consulta banco de dados
    return render(request, 'listar_partidas', {'partidas': partidas})

#Criar uma partida
def criar_partida(request):
    if request.method == 'POST': #indica que o formulário foi enviado
        form = PartidaForm(request.POST)
        if form.is_valid(): #se os dados cumprem os requisitos do formulário
            form.save() #salva no bd
            return redirect('listar_partidas')
    else:
        form = PartidaForm() #mostra um formulário vazio p/ usuário

    return render(request, 'criar_time/games.html', {'form': form})

#para retornar uma lista dinâmica de partidas criadas com json
def listar_partidas_json(request):
    partidas =Criar_Partida.objects.all()
    dados = list(partidas.values('nome_jogo', 'local', 'data', 'hora', 'tipo_jogo', 'tipo_quadra', 'sexo_jogadores'))
    return JsonResponse(dados, safe=False)