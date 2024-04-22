from django.urls import path
from order.apis.cart import *
from order.apis.order import *

urlpatterns = [
    path('get-cart/', GetAllCartItemsAPI.as_view(), name='get-cart'),
    path('get-order/', GetAllOrderItemsAPI.as_view(), name='get-order'),
    path('create-cart/', CreateCartItemsAPI.as_view(), name='create-cart'),
    path('create-order/', CreateOrderItemsAPI.as_view(), name='create-order'),
]
