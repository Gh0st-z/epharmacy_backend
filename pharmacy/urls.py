from django.urls import path
from pharmacy.apis.pharmacy import *

urlpatterns = [
    path('list-pharmacy/', GetAllPharmacyAPI.as_view(), name='list-pharmacy'),
    path('get-pharmacy/', GetPharmacyProfileAPI.as_view(), name='get-pharmacy'),
    path('add-pharmacy/', CreatePharmacyProfileAPI.as_view(), name='add-pharmacy'),
]
