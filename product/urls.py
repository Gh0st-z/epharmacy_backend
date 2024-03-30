from django.urls import path
from product.apis.products import *

urlpatterns = [
    path('add-product/', AddProductAPI.as_view(), name='add-product'),
    path('get-product/', GetProductAPI.as_view(), name='get-product'),
    path('get-medicine/', GetMedicineAPI.as_view(), name='get-medicine'),
]
