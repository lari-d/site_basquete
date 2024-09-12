from django.urls import path
from . import views

urlpatterns = [
    path('partidas/criar', views.criar_partida, name='criar_partida'),
    path('partidas/', views.listar_partidas, name='listar_partidas'),
    path('partidas/json', views.listar_partidas_json, name='listar_partidas_json'),

]