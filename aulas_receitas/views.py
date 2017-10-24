from django.shortcuts import render

from .serializers import AulaReceitaSerializer
from .models import AulaReceita

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateAulaReceita(APIView):
    serializer_class = AulaReceitaSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAulaReceita(APIView):
    serializer_class = AulaReceitaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(AulaReceita.objects.all(), many=True)
        return Response(serializer.data)

class EditAulaReceita(APIView):
    serializer_class = AulaReceitaSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaReceita.objects.get(id_aula_receita=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(AulaReceita.objects.get(id_aula_receita=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteAulaReceita(APIView):
    serializer_class = AulaReceitaSerializer
    
    def get(self, request, id, format=None):
         serializer = self.serializer_class(AulaReceita.objects.get(id_aula_receita=id))
         return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        AulaReceita.objects.get(id_aula_receita=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)