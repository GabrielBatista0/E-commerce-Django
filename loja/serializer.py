from rest_framework import serializers, relations
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields=['id','nome']

class ProdutosSerializer(serializers.ModelSerializer):
    # categoria = serializers.StringRelatedField()
    class Meta:
        model = Produtos
        fields=['id','nome','descricao','preco','qtd_estoque','disponibilidade','foto','categoria']
    # categoria = CategoriaSerializer()
    

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields =['id','nome','data_nascimento','cpf','data_cadastro','user']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields =['id','logradouro','numero','bairro','complemento','cidade','uf','cep','cliente']

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ['id','metodo','cliente','endereco','data_pedido','preco_total','status_pagamento','status_pedido']

class Pedidos_ItenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Itens
        fields = ['id','produto','quantidade','preco_atual','preco_total','pedido']
