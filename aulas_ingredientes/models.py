from django.db import models

from aulas.models import Aula
from ingredientes.models import Ingrediente 

class AulaIngrediente (models.Model):
    id_aula_ingrediente = models.AutoField(primary_key=True)
    id_ingrediente = models.ForeignKey(Ingrediente, related_name='Ingrediente', on_delete=models.CASCADE)
    id_aula = models.ForeignKey(Aula, related_name='Aula', on_delete=models.CASCADE)
    quantidade_projetada_aula = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_utilizada_aula = models.DecimalField(max_digits=10, decimal_places=2)