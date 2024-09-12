from django.urls import path
from . import views

urlpatterns = [
    path('quadras/', views.listar_quadras, name='listar_quadras'),
    path('quadras/json/', views.listar_quadras_json, name='listar_quadras_json'),
    path('quadras/criar/', views.criar_quadra, name='criar_quadra'),
]
