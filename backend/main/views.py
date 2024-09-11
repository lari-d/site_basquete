from django.shortcuts import render, redirect 
from .models import Criar_Partida
from .forms import PartidaForm 

# Create your views here.

#Listar uma partida
def listar_partidas(request):
    partidas = Criar_Partida.objects.all() #consulta banco de dados
    return render(request, '.../criar_time/lista_partidas', {'partidas': partidas})

#Criar uma partida
def criar_partida(request):
    if request.method == 'POST': #indica que o formulário foi enviado
        form = PartidaForm(request.POST)
        if form.is_valid(): #se os dados cumprem os requisitos do formulário
            form.save() #salva no bd
            return redirect('listar_partidas')
    else:
        form = PartidaForm() #mostra um formulário vazio p/ usuário

    return render(request, '.../criar_time/games.html', {'form': form})