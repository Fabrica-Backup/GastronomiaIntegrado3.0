from django.shortcuts import render

from .serializers import (
    CreateAulaIngredienteSerializer,
    ListAulaIngredienteSerializer,
    EditAulaIngredienteSerializer
)
from .models import AulaIngrediente

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateAulaIngrediente(APIView):
    serializer_class = CreateAulaIngredienteSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAulaIngrediente(APIView):
    serializer_class = ListAulaIngredienteSerializer
    
    def get(self, request, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.all(), many=True)
        return Response(serializer.data)

class EditAulaIngrediente(APIView):
    serializer_class = EditAulaIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAulaIngrediente(APIView):
    serializer_class = EditAulaIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        AulaIngrediente.objects.get(id_aula_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)