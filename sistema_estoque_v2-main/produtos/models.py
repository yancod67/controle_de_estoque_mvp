from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    un_medida = models.CharField(max_length=10, default='un' , verbose_name="Unidade de Medida")
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_vencimento = models.DateField(verborse_name="Data de Vencimento", null=True, blank=True)

   
    class Meta:
        verborse_name = "Produtos"
        
    def __str__(self):  
        return self.nome