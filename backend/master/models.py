from django.db import models

# Create your models here.

class Local(models.Model):
    nome=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

#aluguel de quadras
class Quadra(models.Model):
    local =models.ForeignKey(Local, on_delete=models.CASCADE)
    tipo_quadra = models.CharField(max_length=10, choices=[('Fechada', 'Fechada'), ('Aberta', 'Aberta')])

    def __str__(self):
        return f'{self.local} - {self.tipo_quadra}'
    
class Aluguel_Quadra(models.Model):
    quadra=models.ForeignKey(Quadra, on_delete=models.CASCADE)
    data=models.DataField()    
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    nome_responsavel = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'Aluguel de {self.quadra} em {self.data} de {self.hora_inicio} até {self.hora_fim}'