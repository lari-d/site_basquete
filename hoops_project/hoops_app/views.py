from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, QuadraForm, TimeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Quadra, Time
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'html/index/index.html')

def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting login for: {username}")

        # Autentica o usuário
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")

        if user is not None:
            print("Login successful")
            login(request, user)
            return redirect('main')
        else:
            print("Login failed: User or password incorrect")
            messages.error(request, 'Usuário ou senha inválidos')
            return render(request, 'html/tela_login/login2.html')
    else:
        return render(request, 'html/tela_login/login2.html')

def cadastro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica o usuário após o cadastro
            return redirect('main')  # Redireciona para a tela inicial
    else:
        form = UsuarioForm()
    return render(request, 'html/cadastro/cadastro.html', {'form': form})

#Crud quadras
def listar_quadras(request):
    quadras = Quadra.objects.all()
    return render(request, 'quadras/listar.html', {'quadras': quadras})

def criar_quadra(request):
    if request.method == 'POST':
        form = QuadraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_quadras')
    else:
        form = QuadraForm()
    return render(request, 'quadras/criar.html', {'form': form})

def editar_quadra(request, quadra_id):
    quadra = get_object_or_404(Quadra, id=quadra_id)
    if request.method == 'POST':
        form = QuadraForm(request.POST, instance=quadra)
        if form.is_valid():
            form.save()
            return redirect('listar_quadras')
    else:
        form = QuadraForm(instance=quadra)
    return render(request, 'quadras/editar.html', {'form': form})

def deletar_quadra(request, quadra_id):
    quadra = get_object_or_404(Quadra, id=quadra_id)
    if request.method == 'POST':
        quadra.delete()
        return redirect('listar_quadras')
    return render(request, 'quadras/deletar.html', {'quadra': quadra})

def forgot_pass(request):
    return render(request, 'html/esqueceu_a_senha/senha.html')

#@login_required
def main(request):
    return render(request, 'html/tela_principal/inicial.html', {'user' : request.user})