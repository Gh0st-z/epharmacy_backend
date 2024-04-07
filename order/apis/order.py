from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from order.models import Cart
from autho.models import User
from order.serializers.serializers import OrderSerializer

class CreateOrderItemsAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'quantity': request.data.get('quantity'),
            'price': request.data.get('price'),
            'total_price': request.data.get('total_price'),
            'billing_address': request.data.get('billing_address'),
            'status': request.data.get('status')
        }
        customer = request.GET.get('customer_id')
        cart = request.GET.get('cart_id')
        data['customer'] = customer
        data['cart'] = cart

        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
