from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quadra(models.Model):
    nome = models.CharField(max_length=100)
    localização = models.CharField(max_length=200)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Aluguel_Quadra(models.Model):
    quadra=models.ForeignKey(Quadra, on_delete=models.CASCADE)
    data=models.DateField()    
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    nome_responsavel = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'Aluguel de {self.quadra} em {self.data} de {self.hora_inicio} até {self.hora_fim}'