from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    return render(request,'produtos/home.html')


def produtos(request): 
    novo_produto = Produto()
    novo_produto.nome = request.POST.get('nome')
    novo_produto.descricao = request.POST.get('descricao')
    novo_produto.preco = request.POST.get('preco')
    novo_produto.validade = request.POST.get('validade')

    #salvando no BD
    novo_produto.save()

    produtos = dict(
        produtos = Produto.objects.all()

    )

    return render(request, 'produtos/produtos.html')