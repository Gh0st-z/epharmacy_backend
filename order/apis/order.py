from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from order.models import Order
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


class GetAllOrderItemsAPI(APIView):
    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        if order.exists():
            serializer = OrderSerializer(order, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)
