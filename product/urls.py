from django.urls import path
from product.apis.products import *

urlpatterns = [
    path('add-product/', AddProductAPI.as_view(), name='add-product'),
    path('get-product/', GetProductAPI.as_view(), name='get-product'),
    path('get-medicine/', GetMedicineAPI.as_view(), name='get-medicine'),
    path('updget-product/<uuid:id>/', GetProductUpdateDetailAPI.as_view(), name='updget-product'),
    path('updget-medicine/<uuid:id>/', GetMedicineUpdateDetailAPI.as_view(), name='updget-medicine'),
    path('update-product/<uuid:id>/', UpdateProductAPI.as_view(), name='update-product'),
    path('update-medicine/<uuid:id>/', UpdateMedicineAPI.as_view(), name='update-medicine'),
]
