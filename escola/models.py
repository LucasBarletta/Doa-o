from django.db import models

# Create your models here.

class Escola(models.Model):
    nome = models.CharField(max_length=50,verbose_name='Nome')
    diretor = models.CharField(max_length=50, verbose_name='Diretor')
    numeroAlunos = models.IntegerField(verbose_name='Numero de Alunos')
    contatos = models.CharField(max_length=50, verbose_name='Contatos')
    localizacao = models.CharField(max_length=50, verbose_name='Localização')
    email = models.EmailField(verbose_name='Email')
    senha = models.CharField(max_length=50, verbose_name='Senha')

    def __str__(self):
        return self.nome
