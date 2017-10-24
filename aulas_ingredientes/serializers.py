from rest_framework import serializers
from .models import AulaIngrediente
from decimal import *

from ingredientes.serializers import (
    CreateIngredienteSerializer,
    ListIngredienteSerializer,
    EditIngredienteSerializer
)


class CreateAulaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaIngrediente
        fields = [
            'id_aula_ingrediente',
            'id_ingrediente',
            'id_aula',
            'quantidade_projetada_aula',
            'quantidade_utilizada_aula'
        ]
    
    def validate (self, data):
        quantidade_projetada_aula = Decimal (data['quantidade_projetada_aula'])
        quantidade_utilizada_aula = Decimal (data['quantidade_utilizada_aula'])

        if quantidade_projetada_aula < 0:
            raise serializers.ValidationError('O campo quantidade projetada não pode ser negativo')
        elif quantidade_utilizada_aula < 0:
            raise serializers.ValidationError('O campo quantidade utilizada não pode ser negativo')
        return data

class ListAulaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaIngrediente
        fields = [
            'id_aula_ingrediente',
            'id_ingrediente',
            'id_aula',
            'quantidade_projetada_aula',
            'quantidade_utilizada_aula'
        ]

class EditAulaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaIngrediente
        fields = [
            'id_aula_ingrediente',
            'id_ingrediente',
            'id_aula',
            'quantidade_projetada_aula',
            'quantidade_utilizada_aula'
        ]

    def validate (self, data):
        quantidade_projetada_aula = Decimal (data['quantidade_projetada_aula'])
        quantidade_utilizada_aula = Decimal (data['quantidade_utilizada_aula'])

        if quantidade_projetada_aula < 0:
            raise serializers.ValidationError('O campo quantidade projetada não pode ser negativo')
        elif quantidade_utilizada_aula < 0:
            raise serializers.ValidationError('O campo quantidade utilizada não pode ser negativo')
        return data


    