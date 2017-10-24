from rest_framework import serializers
from .models import Aula


class CreateAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = [
            'id_aula',
            'data_aula',
            'descricao_aula',
            'aula_agendada',
            'aula_concluida',
            'periodo_aula',
            'numero_de_alunos_projetados_aula'
        ]
    
    def validate (self, data):
        data_aula = data ['data_aula']
        descricao_aula = data ['descricao_aula']
        aula_agendada = data ['aula_agendada']
        aula_concluida = data ['aula_concluida']
        periodo_aula = data ['periodo_aula']
        numero_de_alunos_projetados_aula = data ['numero_de_alunos_projetados_aula']

        if numero_de_alunos_projetados_aula < 0:
            #validação da data irineu
            raise serializers.ValidationError('O campo número de alunos projetado não pode ser negativo')
        return data

class ListAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = [
            'id_aula',
            'data_aula',
            'descricao_aula',
            'aula_agendada',
            'aula_concluida',
            'periodo_aula',
            'numero_de_alunos_projetados_aula'
        ]

class EditAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = [
            'id_aula',
            'data_aula',
            'descricao_aula',
            'aula_agendada',
            'aula_concluida',
            'periodo_aula',
            'numero_de_alunos_projetados_aula'
        ]

    def validate (self, data):
        data_aula = data ['data_aula']
        descricao_aula = data ['descricao_aula']
        aula_agendada = data ['aula_agendada']
        aula_concluida = data ['aula_concluida']
        periodo_aula = data ['periodo_aula']
        numero_de_alunos_projetados_aula = data ['numero_de_alunos_projetados_aula']

        if numero_de_alunos_projetados_aula < 0:
            #validação da data irineu
            raise serializers.ValidationError('O campo número de alunos projetado não pode ser negativo')
        return data
