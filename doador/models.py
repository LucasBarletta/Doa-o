from django.db import models

# Create your models here.

class Doador(models.Model):
    nome= models.CharField(
        max_length=50,
        verbose_name= 'Nome'
    )
    idade= models.IntegerField(
        verbose_name='idade'
    )
    localizacao= models.CharField(
        max_length=50,
        verbose_name='localizaçao'
    )
    cpf= models.CharField(
        max_length=50,
        verbose_name='cpf'
    )
    email= models.EmailField(
        max_length=50,
        verbose_name='email'
    )
    senha= models.CharField(
        max_length=50,
        verbose_name='senha'
    )
    def __str__(self):
        return self.nome