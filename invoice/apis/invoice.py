from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from order.models import Order
from autho.models import User
from invoice.serializers.serializers import InvoiceSerializer

class GenerateInvoiceAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'quantity': request.data.get('quantity'),
            'total_price': request.data.get('total_price'),
            'billing_address': request.data.get('billing_address'),
        }
        customer = request.GET.get('customer_id')
        order = request.GET.get('order_id')
        data['customer'] = customer
        data['product'] = product

        serializer = InvoiceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
