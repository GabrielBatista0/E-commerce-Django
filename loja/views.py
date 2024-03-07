from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import *
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

class CategoriaList(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )
    #query set busca info do banco
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoList(ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )    
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

class ProdutosDetails(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, )    
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

class EnderecoList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )    
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EnderecoDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

#jeito mais facil, uma view faz todas as operações
class ClientesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
    def get_queryset(self):
        queryset = Clientes.objects.all()         
        email = self.request.query_params.get('email')
        if email is not None:
            usuario =  get_object_or_404(Clientes, user__email=email)
            if usuario is not None:
                queryset = queryset.filter(user=usuario.id)
            return queryset
        else:
            queryset = Clientes.objects.all()
            return queryset
        
    

class PedidosList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

class PedidosDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

class Pedido_ItensList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Pedido_Itens.objects.all()
    serializer_class = Pedidos_ItenSerializer

class Pedido_ItensDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Pedido_Itens.objects.all()
    serializer_class = Pedidos_ItenSerializer
