from django.shortcuts import render


from .serializers import CreateAulaSerializer, ListAulaSerializer, EditAulaSerializer
from .models import Aula

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateAula(APIView):
    serializer_class = CreateAulaSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ListAula(APIView):
    serializer_class = ListAulaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Aula.objects.all(), many=True)
        return Response(serializer.data)


class EditAula(APIView):
    serializer_class = EditAulaSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Aula.objects.get(id_aula=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(Aula.objects.get(id_aula=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAula(APIView):
    serializer_class = ListAulaSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Aula.objects.get(id_aula=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        Aula.objects.get(id_aula=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class planejar_aulas(APIView):

    def aulas (request):
        return render(request, 'aulas/planejar_aulas.html', {})

class aulas_concluidas(APIView):
    
    def aulas (request):
        return render(request, 'aulas/aulas-concluidas.html', {})
