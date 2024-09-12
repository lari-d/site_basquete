from django.db import models

# Create your models here.

class Local(models.Model):
    nome=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Criar_Partida(models.Model):
    name_jogo=models.CharField(max_lenght=200)
    local = models.ForeignKey(Local, on_delete=models.CASCADE) #chave estrangeira
    data=models.DateField()
    hora = models.TimeField()
    tipo_jogo = models.CharField(max_length=10, choices=[('3x3', '3,3'), ('5x5', '5x5')])#primeiro valor é salvo no bd e segundo aparece para o usuário
    tipo_quadra = models.CharField(max_length=10, choices=[('Fechada', 'Fechada'), ('Aberta', 'Aberta')])
    sexo_jogadores = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Misto', 'Misto')])

    def __str__(self): # transforma os valores em strind
        return f'{self.nome_jogo} em {self.local}' #exemplo: final de campionato em ginásio municipal 


    