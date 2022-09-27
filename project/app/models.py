from django.db import models

# Create your models here.
class Atividades(models.Model):
    descricao = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    prazo = models.CharField(max_length=10)