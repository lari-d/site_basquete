from django.db import models
from django.contrib.auth.models import AbstractUser

'''class Local(models.Model):
    nome=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Criar_Partida(models.Model):
    name_jogo=models.CharField(max_lenght=200)
    local = models.ForeignKey(Local, on_delete=models.CASCADE) #chave estrangeira
    data=models.DataField()
    hora = models.TimeField()
    tipo_jogo = models.CharField(max_length=10, choices=[('3x3', '3,3'), ('5x5', '5x5')])#primeiro valor é salvo no bd e segundo aparece para o usuário
    tipo_quadra = models.CharField(max_length=10, choices=[('Fechada', 'Fechada'), ('Aberta', 'Aberta')])
    sexo_jogadores = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Misto', 'Misto')])

    def __str__(self): # transforma os valores em strind
        return f'{self.nome_jogo} em {self.local}' #exemplo: final de campionato em ginásio municipal 
'''
class Usuario(AbstractUser):  # Herda de AbstractUser para utilizar o sistema de autenticação do Django
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('Outro', 'Outro')], blank=True)

    class meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    # Aqui estamos definindo um related_name único para os grupos e permissões
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='hoops_app_usuario_set',
        blank=True,
        help_text='Os grupos aos quais este usuário pertence.',
        verbose_name='grupos'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='hoops_app_usuario_permissions_set',
        blank=True,
        help_text='Permissões específicas para este usuário.',
        verbose_name='permissões do usuário'
    )

    def __str__(self):
        return self.username
        

class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    jogadores = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome
    
class Quadra(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=200)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
