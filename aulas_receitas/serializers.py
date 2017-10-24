from rest_framework import serializers
from .models import AulaReceita
from aulas.serializers import (
    CreateAulaSerializer,
    ListAulaSerializer,
    EditAulaSerializer
)
from receitas.serializers import (
    CreateReceitaSerializer,
    ListReceitaSerializer,
    EditReceitaSerializer
)

class AulaReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaReceita
        fields = [
            'id_aula_receita',
            'id_aula',
            'id_receita'
        ]
    

