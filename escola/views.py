from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, serializers
from doar.models import Doar

from escola.models import Escola
from rest_framework.decorators import action
from escola.serializers import EscolaSerializer
from rest_framework.response import Response
from rest_framework import status

class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    # permission
    # token
    serializer_class = EscolaSerializer

    @action(detail=False, methods=['POST'])
    def Login(self, request):
        try:
            escola = Escola.objects.get(email=request.data['email'])

            if escola.senha == request.data['senha']:
                return Response({'mensagem': 'Logado'})
            else:
                return Response({'mensagem': 'Senha incorreta'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Escola.DoesNotExist:
            return Response ({'mensagem': 'email nao encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def aceitar(self, request, pk=None):
        doacao = Doar.objects.get(pk=request.data['doacao'])
        doacao.escola = self.get_object()
        doacao.save(update_fields=['escola'])
        return Response({'message': 'doado'})

