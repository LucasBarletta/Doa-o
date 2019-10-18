from rest_framework import serializers
from escola.models import Escola
from doador.serializers import DoadorSerializer
from doador.models import Doador
from doar.models import Doar

class EscolaData(serializers.Serializer):
    nome = serializers.CharField(read_only=True)

class DoarSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=50)
    quantidade = serializers.IntegerField(read_only=True)
    doador = DoadorSerializer(
        many=True,
        read_only=True,
    )
    escola_doar = EscolaData()

    def create(self, validated_data):
        escola_data = validated_data.pop('escola_doar')
        escola = Escola.objects.get(id=escola_data['id'])
        doar = Doar.objects.create(escola_doar=escola, **validated_data)
        return doar
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.quantidade = validated_data.get('quantidade')
        escola_data = validated_data.pop('escola_doar')
        escola = Escola.objects.get(id=escola_data['id'])
        instance.escola_data = escola
        instance.save()
        return instance