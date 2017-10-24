from django.db import models
import datetime
from django.core.validators import MaxValueValidator

class Aula(models.Model):
    id_aula = models.AutoField(primary_key = True)
    data_aula = models.DateField(default='01 de janeiro de 2000', null = True)
    descricao_aula = models.CharField(max_length = 200)
    aula_agendada = models.BooleanField(default= True)
    aula_concluida = models.BooleanField(default= True)
    periodo_aula = models.CharField(max_length = 100, null=True)
    numero_de_alunos_projetados_aula = models.PositiveIntegerField(validators=[MaxValueValidator(50)], null=True)

