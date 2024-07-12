from django.db import models

from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio


class Veiculo(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    ano = models.IntegerField(default=0, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    cor = models.ForeignKey(Cor, on_delete=models.RESTRICT)
    acessorios = models.ManyToManyField(Acessorio)

    def __str__(self):
        return f'{self.modelo.nome} - {self.ano} - {self.cor}'