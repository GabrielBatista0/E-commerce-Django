from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.SimpleRouter()
router.register('clientes', views.ClientesViewSet)

urlpatterns = [
    path('produtos/', view= views.ProdutoList.as_view()),
    path('produtos/<int:pk>/', view= views.ProdutosDetails.as_view()),
    path('categorias/', view= views.CategoriaList.as_view()),
    path('categorias/<int:pk>/', view= views.CategoriaDetails.as_view()),
    path('endereco/', view= views.EnderecoList.as_view()),
    path('endereco/<int:pk>/', view= views.EnderecoDetails.as_view()),
    path('pedidos/', view= views.PedidosList.as_view()),
    path('pedidos/<int:pk>/', view= views.PedidosDetails.as_view()),
    path('pedidositens/', view= views.Pedido_ItensList.as_view()),
    path('pedidositens/<int:pk>/', view= views.Pedido_ItensDetails.as_view()),
 ]+ router.urls