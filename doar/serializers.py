from rest_framework import serializers
from escola.models import Escola
from doador.serializers import DoadorSerializer
from doador.models import Doador

class EscolaData(serializers.Serializer):
    nome = serializers.CharField(read_only=True)

class DoarSerializer(serializers.Serializer):