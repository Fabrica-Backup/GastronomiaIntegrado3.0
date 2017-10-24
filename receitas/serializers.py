from rest_framework import serializers

from .models import Receita
from categorias.serializers import CategoriaSerializer
from classificacoes.serializers import ClassificacaoSerializer

class CreateReceitaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer
    classificacoes = ClassificacaoSerializer
    class Meta:
        model = Receita
        fields = [
            'id_receita',
            'id_categoria',
            'id_classificacao',
            'nome_receita',
            'modo_preparo_receita'

        ]
    def validade (self, data):
        nome_receita = data['nome_receita']
        modo_preparo_receita = data['modo_preparo_receita']
        nome_receita_qs = Receita.objects.filter(nome_receita=nome_receita)

        if nome_receita_qs.exists():
            raise serializers.ValidationError('Já existe uma receita cadastrada com este nome')
        elif nome_receita > 100:
            raise serializers.ValidationError('O nome da receita não pode ter mais de 100 caracteres')
        return data 

class ListReceitaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer
    classificacoes = ClassificacaoSerializer
    class Meta:
        model = Receita
        fields = [
            'id_receita',
            'id_categoria',
            'id_classificacao',
            'nome_receita',
            'modo_preparo_receita'
        ]

class EditReceitaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer
    classificacoes = ClassificacaoSerializer
    class Meta:
        model = Receita
        fields = [
            'id_receita',
            'id_categoria',
            'id_classificacao',
            'nome_receita',
            'modo_preparo_receita'
        ]

    def validade (self, data):
        nome_receita = data['nome_receita']
        modo_preparo_receita = data['modo_preparo_receita']
        nome_receita_qs = Receita.objects.filter(nome_receita=nome_receita)

        if nome_receita_qs.exists():
            raise serializers.ValidationError('Já existe uma receita cadastrada com este nome')
        elif nome_receita > 100:
            raise serializers.ValidationError('O nome da receita não pode ter mais de 100 caracteres')
        return data 

