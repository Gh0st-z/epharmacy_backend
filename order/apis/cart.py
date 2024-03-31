from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from product.models import Product
from autho.models import User
from order.serializers.serializers import CartSerializer

class CreateCartItemsAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'quantity': request.data.get('quantity'),
            'price': request.data.get('price'),
            'total_price': request.data.get('total_price'),
        }
        customer = request.data.get('customer_id')
        product = request.data.get('product_id')
        data['customer'] = customer
        data['product'] = product
        prescription = request.FILES.get('prescription')

        if prescription:
            data['prescription'] = prescription

        serializer = CartSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
