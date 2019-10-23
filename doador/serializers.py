from rest_framework import serializers
from doador.models import Doador

class DoadorSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)
    idade = serializers.IntegerField()
    localizacao = serializers.CharField(max_length=50)
    cpf = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    senha = serializers.CharField(max_length=255)
    


    def create(self,validated_data):
        doador = Doador.objects.create(**validated_data)
        return doador

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance