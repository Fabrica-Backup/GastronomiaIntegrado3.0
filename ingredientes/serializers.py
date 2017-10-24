from decimal import *

from rest_framework import serializers

from .models import Ingrediente
from unidades_medida.serializers import UnidadeMedidaSerializer

class CreateIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_calorica_ingrediente',
            'aproveitamento_ingrediente',
            'id_unidade_medida'
        ]
    
    def validate(self, data):
        nome_ingrediente = data['nome_ingrediente']
        quantidade_calorica_ingrediente = Decimal(data['quantidade_calorica_ingrediente'])
        aproveitamento_ingrediente = Decimal(data['aproveitamento_ingrediente'])
        nome_qs = Ingrediente.objects.filter(nome_ingrediente=nome_ingrediente)
        
        if nome_qs.exists():
            raise serializers.ValidationError('Já existe um ingrediente cadastrado com este nome')
        elif quantidade_calorica_ingrediente < 0:
            raise serializers.ValidationError('O campo quantidade calorica não pode ser negativo')
        elif aproveitamento_ingrediente < 0:
            raise serializers.ValidationError('O campo aproveitamento ingrediente não pode ser negativo')
        elif aproveitamento_ingrediente > 100:
            raise serializers.ValidationError('O aproveitamento não pode ser acima de 100')
        return data 
      

class ListIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_calorica_ingrediente',
            'aproveitamento_ingrediente',
            'quantidade_estoque_ingrediente',
            'quantidade_reservada_ingrediente',
            'valor_ingrediente',
            'motivo_retirada_estoque',
            'id_unidade_medida'
        ]

class EditIngredienteSerializer(serializers.ModelSerializer):
    unidades_medida = UnidadeMedidaSerializer
    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_calorica_ingrediente',
            'aproveitamento_ingrediente',
            'quantidade_estoque_ingrediente',
            #quantidade_reservada_ingrediente
            'valor_ingrediente',
            'motivo_retirada_estoque',
            'id_unidade_medida'
        ]


   
    def validate(self, data):
        quantidade_calorica_ingrediente = Decimal(data['quantidade_calorica_ingrediente'])
        aproveitamento_ingrediente = Decimal(data['aproveitamento_ingrediente'])
        #quantidade_estoque_ingrediente = Decimal(data['quantidade_estoque_ingrediente'])
        #quantidade_reservada_ingrediente = Decimal(data['quantidade_reservada_ingrediente'])
        valor_ingrediente = Decimal(data['valor_ingrediente'])

        if quantidade_calorica_ingrediente < 0:
            raise serializers.ValidationError('O campo quantidade calorica não pode ser negativo')
        elif aproveitamento_ingrediente < 0:
            raise serializers.ValidationError('O Campo aproveitamento não pode ser negativo')
        elif aproveitamento_ingrediente > 100:
            raise serializers.ValidationError('O aproveitamento não pode ser acima de 100')
        #elif quantidade_estoque_ingrediente < 0:
         #   raise serializers.ValidationError('O campo quantidade em estoque não pode ser negativo')
        #elif quantidade_reservada_ingrediente < 0:
            #raise serializers.ValidationError('O Campo quantidade reservada não pode ser negativo')
        elif valor_ingrediente < 0:
            raise serializers.ValidationError('O campo valor ingrediente não pode ser negativo')
        return data

    def update(self, instance, validated_data):
        print("pegando nome_Ingrediente")
        instance.nome_ingrediente = validated_data.get('nome_ingrediente', instance.nome_ingrediente)
        print("pegando quantidade_calorica")
        instance.quantidade_calorica_ingrediente = validated_data.get('quantidade_calorica_ingrediente', instance.quantidade_calorica_ingrediente)
        print("pegando aproveitamento_ingrediente")
        instance.aproveitamento_ingrediente = validated_data.get('aproveitamento_ingrediente', instance.aproveitamento_ingrediente)
        print("pegando a quantidade e somando")
        instance.quantidade_estoque_ingrediente = validated_data.get('quantidade_estoque_ingrediente', instance.quantidade_estoque_ingrediente) + instance.quantidade_estoque_ingrediente
        print("pegando o valor")
        instance.valor_ingrediente = validated_data.get('valor_ingrediente', instance.valor_ingrediente)
        print("pegando motivo")
        instance.motivo_retirada_estoque = validated_data.get('motivo_retirada_estoque', instance.motivo_retirada_estoque)
        instance.save()
        return instance

        """print ("pegando o + do front")
        if validated_data['quantidade_estoque_ingrediente'] == '+':
            print("somando do front com o back")
            instance.quantidade_estoque_ingrediente = validated_data.get('quantidade_estoque_ingrediente', 0) + instance.quantidade_estoque_ingrediente
            print("subtraindo")
        elif validated_data['quantidade_estoque_ingrediente'] == '-':
            instance.quantidade_estoque_ingrediente = validated_data.get('quantidade_estoque_ingrediente', 0) - instance.quantidade_estoque_ingrediente
        else: 
            print("editar")
            instance.quantidade_estoque_ingrediente = validated_data.get('quantidade_estoque_ingrediente', instance.quantidade_estoque_ingrediente)
            print("salvando")
            instance.save()
        return instance"""
