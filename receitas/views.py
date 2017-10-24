from django.shortcuts import render

from .models import Receita
from .serializers import CreateReceitaSerializer, ListReceitaSerializer, EditReceitaSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateReceita(APIView):
    serializer_class = CreateReceitaSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListReceita(APIView):
    serializer_class = ListReceitaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Receita.objects.all(), many=True)
        return Response(serializer.data)


class EditReceita(APIView):
    serializer_class = EditReceitaSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Receita.objects.get(id_receita=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(Receita.objects.get(id_receita=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteReceita(APIView):
    serializer_class = EditReceitaSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Receita.objects.get(id_receita=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        Receita.objects.get(id_receita=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)