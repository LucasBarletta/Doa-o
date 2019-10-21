from django.db import models

# Create your models here.
from doador.models import Doador
from escola.models import Escola

class Doar(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    doador = models.ForeignKey(Doador, on_delete=models.SET_NULL, null=True)
    escola = models.ForeignKey(Escola, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
