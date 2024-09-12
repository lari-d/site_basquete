from django.shortcuts import render, redirect 
from .models import Criar_Partida, UserProfile
from .forms import PartidaForm
from django.http import HttpRequest
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.

def pagina_inicial(request):
    return render(request, 'tela_principal/inicial.html')

#Listar uma partida
def listar_partidas(request):
    partidas = Criar_Partida.objects.all()  # consulta o banco de dados
    return render(request, 'criar_time/lista_partidas.html', {'partidas': partidas})

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

def cadastro(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username') # toca nome pra username pois padrão django
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        password = request.POST.get('senha')
        cpassword = request.POST.get('confirmar-senha') 
        altura = request.POST.get('altura')
        posicao = request.POST.get('posicao')
        # if validar_cadastro(request):
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'E-mail já está em uso!')
            return redirect('cadastro')
        
        if password != cpassword:
            messages.add_message(request, messages.ERROR, 'Por favor digite duas senhas iguais!')
            return redirect('cadastro')
        
        novo_usuario = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        UserProfile.objects.create( # não tá funcionando :/
            user=novo_usuario,
            telefone=telefone,
            altura=altura,
            posicao=posicao
        )
        login(request, novo_usuario)
        messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('pagina_inicial')
    else:
        return render(request, 'cadastro/cadastro.html')  # vai pro cadastro se for get