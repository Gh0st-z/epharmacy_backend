from django.urls import path
from order.apis.cart import *
from order.apis.order import *

urlpatterns = [
    path('create-cart/', CreateCartItemsAPI.as_view(), name='create-cart'),
    path('create-order/', CreateOrderItemsAPI.as_view(), name='create-order'),
]
