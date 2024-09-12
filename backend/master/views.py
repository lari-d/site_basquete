from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AluguelQuadra, Quadra, Local
from .forms import AluguelQuadraForm

#listar uma quadra para html
def listar_quadras(request):
    if request.method == 'GET':
        quadras = Quadra.objects.all()
        return render(request, 'aluguel_quadras/listar_quadras.html', {'quadras': quadras})

#criar uma quadra
def criar_quadra(request):
    if request.method == 'POST':
        form = AluguelQuadraForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = AluguelQuadraForm()
    return render(request, 'aluguel_quadras/criar_quadras.html', {'form': form})

#retornar uma lista dinâmica de quadras disponíveis
def listar_quadras_json(request):
    if request.method == 'GET':
        quadras = Quadra.objects.all()
        dados = list(quadras.values('local', 'tipo-quadra'))
        return JsonResponse(dados, safe=False)

