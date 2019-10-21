from rest_framework import serializers

from doar.models import Doar


class DoarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doar
        fields = ['id','nome','doador','escola','descricao']