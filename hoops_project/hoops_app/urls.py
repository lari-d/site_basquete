from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_views, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('forgot_pass/', views.forgot_pass, name='esqueceu senha'),
    path('main/', views.main, name='main'),

    path('quadras/', views.listar_quadras, name='listar_quadras'),
    path('quadras/criar/', views.criar_quadra, name='criar_quadra'),
    path('quadras/editar/<int:quadra_id>/', views.editar_quadra, name='editar_quadra'),
    path('quadras/deletar/<int:quadra_id>/', views.deletar_quadra, name='deletar_quadra'),
]