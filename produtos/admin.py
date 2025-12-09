from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade', 'un_medida', 'vencimento','data_registro')
    search_fields = ('nome',)
