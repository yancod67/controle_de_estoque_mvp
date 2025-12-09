from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    un_medida = models.CharField(max_length=20, default='unidade')
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    vencimento = models.DateField(null=True, blank=True)

    def __str__(self):  
        return self.nome
