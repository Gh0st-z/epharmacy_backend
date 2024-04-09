from django.urls import path
from invoice.apis.invoice import GenerateInvoiceAPI, GetInvoiceAPI

urlpatterns = [
    path('generate-invoice/', GenerateInvoiceAPI.as_view(), name='generate-invoice'),
    path('get-invoice/', GetInvoiceAPI.as_view(), name='get-invoice'),
]
