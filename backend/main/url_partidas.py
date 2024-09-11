from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_partida, name='criar_partida'),
    path('listar/', views.listar_partidas, name='listar_partidas'),
]