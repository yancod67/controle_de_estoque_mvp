from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('id')
    return render(request, 'produtos/listar.html', {'produtos': produtos})

@login_required(login_url='login')
def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        preco = request.POST.get('preco', '0').strip()
        quantidade = request.POST.get('quantidade', '0').strip()
        un_medida = request.POST.get('un_medida', 'unidade').strip()
        data_vencimento = request.POST.get('data_vencimento') or None 

        errors = []
        if not nome:
            errors.append('Nome é obrigatório.')
        try:
            preco_val = float(preco)
            if preco_val < 0:
                errors.append('Preço deve ser >= 0.')
        except ValueError:
            errors.append('Preço inválido.')
        try:
            quantidade_val = int(float(quantidade))
            if quantidade_val < 0:
                errors.append('Quantidade deve ser >= 0.')
        except ValueError:
            errors.append('Quantidade inválida.')

        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'produtos/criar.html', {
                'nome': nome,
                'descricao': descricao,
                'preco': preco,
                'quantidade': quantidade,
                'un_medida' : un_medida,
                'data_vencimento' : data_vencimento
            })

        Produto.objects.create(nome=nome, descricao=descricao, preco=preco_val, quantidade=quantidade_val,un_medida=un_medida, data_vencimento=data_vencimento)
        messages.success(request, 'Produto criado com sucesso.')
        return redirect(reverse('produtos:listar_produtos'))

    return render(request, 'produtos/criar.html')

@login_required(login_url='login')
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        preco = request.POST.get('preco', '0').strip()
        quantidade = request.POST.get('quantidade', '0').strip()
        un_medida = request.POST.get('un_medida', produto.un_medida).strip()
        data_vencimento = request.POST.get('data_vencimento') or None

        errors = []
        if not nome:
            errors.append('Nome é obrigatório.')
        try:
            preco_val = float(preco)
            if preco_val < 0:
                errors.append('Preço deve ser >= 0.')
        except ValueError:
            errors.append('Preço inválido.')
        try:
            quantidade_val = int(float(quantidade))
            if quantidade_val < 0:
                errors.append('Quantidade deve ser >= 0.')
        except ValueError:
            errors.append('Quantidade inválida.')

        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'produtos/editar.html', {'produto': produto})

        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco_val
        produto.quantidade = quantidade_val
        produto.un_medida = un_medida
        produto.data_vencimento = data_vencimento
        produto.save()
        messages.success(request, 'Produto atualizado.')
        return redirect(reverse('produtos:listar_produtos'))

    return render(request, 'produtos/editar.html', {'produto': produto})

@login_required(login_url='login')
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído.')
        return redirect(reverse('produtos:listar_produtos'))
    return render(request, 'produtos/excluir.html', {'produto': produto})
