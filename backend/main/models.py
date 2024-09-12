from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # pegando todas as informações do User da biblioteca padrao do Django
                                                                # (nome, email, senha) e adicionando as coisas extras
    telefone = models.CharField(max_length=15, blank=True, null=True)
    altura = models.CharField(max_length=10, blank=True, null=True)
    posicao = models.CharField(max_length=50, blank=True, null=True)

class Local(models.Model):
    nome=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Criar_Partida(models.Model):
    name_jogo=models.CharField(max_length=200)
    local = models.ForeignKey(Local, on_delete=models.CASCADE) #chave estrangeira
    data=models.DateField()
    hora = models.TimeField()
    tipo_jogo = models.CharField(max_length=10, choices=[('3x3', '3,3'), ('5x5', '5x5')])#primeiro valor é salvo no bd e segundo aparece para o usuário
    tipo_quadra = models.CharField(max_length=10, choices=[('Fechada', 'Fechada'), ('Aberta', 'Aberta')])
    sexo_jogadores = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Misto', 'Misto')])

    def __str__(self): # transforma os valores em strind
        return f'{self.name_jogo} em {self.local}' #exemplo: final de campionato em ginásio municipal 

#aluguel de quadras
class Quadra(models.Model):
    local =models.ForeignKey(Local, on_delete=models.CASCADE)
    tipo_quadra = models.CharField(max_length=10, choices=[('Fechada', 'Fechada'), ('Aberta', 'Aberta')])

    def __str__(self):
        return f'{self.local} - {self.tipo_quadra}'
    
class Aluguel_Quadra(models.Model):
    quadra=models.ForeignKey(Quadra, on_delete=models.CASCADE)
    data=models.DateField()    
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    nome_responsavel = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'Aluguel de {self.quadra} em {self.data} de {self.hora_inicio} até {self.hora_fim}'
    