from django.db import models

# Create your models here.
from doador.models import Doador
from escola.models import Escola

class Doar(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    quantidade = models.IntegerField(max_length=10, verbose_name='Quantidade')
    doador = models.ManyToManyField(
        Doador,
        verbose_name='doador',
    )
    localizacao_escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='localizaçao',
        verbose_name='localizaçao',
    )
    def __str__(self):
        return self.nome