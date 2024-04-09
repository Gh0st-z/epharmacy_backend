from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from order.models import Order
from autho.models import User
from invoice.models import Invoice
from invoice.serializers.serializers import InvoiceSerializer

class GenerateInvoiceAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = dict()
        customer = request.GET.get('customer_id')
        order = request.GET.get('order_id')
        user = User.objects.get(id=customer)
        customer_order = Order.objects.get(order_id=order)

        if user.middle_name == " ":
            data['customer_name'] = user.first_name + " " + user.last_name
        else:
            data['customer_name'] = user.first_name + " " + user.middle_name + " " + user.last_name

        data['quantity'] = customer_order.quantity
        data['total_price'] = customer_order.total_price
        data['billing_address'] = customer_order.billing_address
        data['customer'] = customer
        data['order'] = order

        serializer = InvoiceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetInvoiceAPI(APIView):
    def get(self, request, *args, **kwargs):
        customer = request.GET.get('customer_id')
        invoice = Invoice.objects.filter(customer=customer)

        if invoice.exists():
            serializer = InvoiceSerializer(invoice, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)
