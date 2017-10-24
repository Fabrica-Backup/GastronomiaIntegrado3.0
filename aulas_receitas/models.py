from django.db import models
from aulas.models import Aula
from receitas.models import Receita


class AulaReceita (models.Model):
    id_aula_receita = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(Aula, related_name='Aula_Receita', on_delete=models.CASCADE)
    id_receita = models.ForeignKey(Receita, related_name='Receita', on_delete=models.CASCADE)

