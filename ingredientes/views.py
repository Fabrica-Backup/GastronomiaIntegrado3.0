from django.shortcuts import render

from .models import Ingrediente
from .serializers import CreateIngredienteSerializer, ListIngredienteSerializer, EditIngredienteSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateIngrediente(APIView):
    serializer_class = CreateIngredienteSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListIngrediente(APIView):
    serializer_class = ListIngredienteSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Ingrediente.objects.all(), many=True)
        return Response(serializer.data)

class EditIngrediente(APIView):
    serializer_class = EditIngredienteSerializer

    def get(self, request, id, format=None):
        print("get do ingrediente")
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id))
        print("serializado ok")
        return Response(serializer.data)

    def post(self, request, id, format=None):
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id), data=request.data)
        print(id)
        if serializer.is_valid():
            print("salvando")
            serializer.save()
            print("gerando response")
            return Response(serializer.data)

        print("serializer errado")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteIngrediente(APIView):
    serializer_class = EditIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        Ingrediente.objects.get(id_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

