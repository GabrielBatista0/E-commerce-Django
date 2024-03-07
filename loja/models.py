from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.nome  
    
class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.PositiveIntegerField()
    disponibilidade = models.BooleanField(default=True)
    foto = models.ImageField(upload_to="produtos")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    
class Clientes(models.Model):
    # CLIENTE_PF = 'F'
    # CLIENTE_PJ = 'J'
    # TIPOS_CLIENTES =[
    #     (CLIENTE_PF,"Pessoa Física"),
    #     (CLIENTE_PJ,"Pessoa Juridica")
    # ]

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14,unique=True)
    data_cadastro = models.DateField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    telefone = models.CharField(max_length=14)
        
class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)


class Pedidos(models.Model):
    STATUS_PG_NEGADO = 'N'
    STATUS_PG_PENDENTE = 'P'
    STATUS_PG_APROVADO = 'A'
    STATUS_PG_CHOICES = (
        (STATUS_PG_NEGADO,'NEGADO'),
        (STATUS_PG_PENDENTE, 'PENDENTE'),
        (STATUS_PG_APROVADO,'APROVADP')
    )

    STATUS_PD_ENTREGUE = 'E'
    STATUS_PD_CANCELADO = 'C'
    STATUS_PD_TRANSPORTE = 'T'
    STATUS_PD_PREPARACAO = 'P'
    STATUS_PD_AGUARDANDO = 'A'
    
    STATUS_PD_CHOICES = (
        (STATUS_PD_ENTREGUE,'Entregue'),
        (STATUS_PD_CANCELADO, 'Cancelado'),
        (STATUS_PD_TRANSPORTE,'Transporte'),
        (STATUS_PD_PREPARACAO,'Preparação'),
        (STATUS_PD_AGUARDANDO,'Aguardando')
    )
    PAGAMENTO_PIX = 'P'
    PAGAMENTO_CARTAO = 'C'
    PAGAMENTO_BOLETO = 'B'
    PAGAMENTO_CHOICES = [
        (PAGAMENTO_PIX,'PIX'),
        (PAGAMENTO_CARTAO, 'CARTÃO'),
        (PAGAMENTO_BOLETO,'BOLETO')
    ]
    metodo = models.CharField(max_length=1, choices=PAGAMENTO_CHOICES ,default=PAGAMENTO_PIX)
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    data_pedido = models.DateField(auto_now=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    status_pagamento = models.CharField(max_length=1, choices=STATUS_PG_CHOICES , default=STATUS_PG_PENDENTE)
    status_pedido = models.CharField(max_length=1, choices=STATUS_PD_CHOICES, default=STATUS_PD_AGUARDANDO)


class Pedido_Itens(models.Model):
    produto = models.ForeignKey(Produtos,on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_atual = models.DecimalField(max_digits=6, decimal_places=2)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2 )
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
