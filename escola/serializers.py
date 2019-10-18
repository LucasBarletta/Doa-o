from rest_framework import serializers
from escola.models import Escola

class EscolaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)

    def create(self, validated_data):
        escola = Escola.objects.create(**validated_data)
        return escola
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance