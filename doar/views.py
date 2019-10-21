from django.shortcuts import render
from rest_framework import viewsets, views

from doar.serializers import DoarSerializer
from doar.models import Doar
from rest_framework.response import Response
from rest_framework.decorators import action


class DoarViewSet(viewsets.ModelViewSet):
    queryset = Doar.objects.all()
    serializer_class = DoarSerializer

    @action(detail=False, methods=['GET'])
    def disponiveis(self, request):
        doacoes = Doar.objects.all().filter(escola__isnull=True)
        return Response(DoarSerializer(doacoes, many=True).data)

