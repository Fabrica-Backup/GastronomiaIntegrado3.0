from django.db import models
from classificacoes.models import Classificacao
from categorias.models import Categoria

class Receita (models.Model):
    id_receita = models.AutoField(primary_key = True)
    id_categoria = models.ForeignKey(Categoria, related_name = 'categoria', on_delete = models.CASCADE)
    id_classificacao = models.ForeignKey(Classificacao, related_name='classificacao', on_delete = models.CASCADE)
    nome_receita = models.CharField(max_length = 100)
    modo_preparo_receita = models.TextField(max_length = 6500)

