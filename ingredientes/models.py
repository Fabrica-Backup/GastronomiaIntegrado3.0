from django.db import models

from unidades_medida.models import UnidadeMedida

class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key = True)
    nome_ingrediente = models.CharField(max_length = 200)
    quantidade_calorica_ingrediente = models.DecimalField(max_digits = 6, decimal_places = 1)
    aproveitamento_ingrediente = models.DecimalField(max_digits = 4, decimal_places = 1)
    quantidade_estoque_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)
    quantidade_reservada_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)
    valor_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0) 
    motivo_retirada_estoque = models.CharField(max_length = 200 , null = True)
    id_unidade_medida = models.ForeignKey(UnidadeMedida, null=True, related_name = 'id_unidades_medida', on_delete = models.CASCADE)

