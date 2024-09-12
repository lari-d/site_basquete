from django.shortcuts import render, redirect, get_object_or_404
from .models import Quadra, Time
from .forms import UsuarioForm, QuadraForm, TimeForm

# Create your views here.

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