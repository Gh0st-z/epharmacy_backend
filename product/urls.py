from django.urls import path
from product.apis.products import *

urlpatterns = [
    path('add-product/', AddProductAPI.as_view(), name='add-product'),
]
