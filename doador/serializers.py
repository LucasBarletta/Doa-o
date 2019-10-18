from rest_framework import serializers
from doador.models import Doador

class DoadorSerializer(serializers.Serializer):
    nome= serializers.CharField(max_length=50)

    def create(self,validated_data):
        doador = Doador.objects.create(**validated_data)
        return doador

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance