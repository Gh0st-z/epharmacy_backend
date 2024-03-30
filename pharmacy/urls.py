from django.urls import path
from pharmacy.apis.pharmacy import *

urlpatterns = [
    path('get-pharmacy/', GetPharmacyProfileAPI.as_view(), name='get-pharmacy'),
    path('add-pharmacy/', CreatePharmacyProfileAPI.as_view(), name='add-pharmacy'),
]
