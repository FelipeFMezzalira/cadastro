from django.db import models

# Create your models here.

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField()
    descricao = models.TextField()
    preco = models.FloatField()
    validade = models.DateField()

