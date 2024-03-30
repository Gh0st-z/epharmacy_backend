from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from pharmacy.models import Pharmacy
from product.models import Product
from product.serializers.serializers import ProductSerializer

class AddProductAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'product_name': request.data.get('product_name'),
            'product_info': request.data.get('product_info'),
            'price': request.data.get('price'),
            'product_type': request.data.get('product_type'),
            'quantity': request.data.get('quantity'),
        }

        pharmacy_id = request.data.get('pharmacy_id')
        data['pharmacy'] = pharmacy_id
        product_image = request.FILES.get('product_image')

        if product_image:
            data['product_image'] = product_image

        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
