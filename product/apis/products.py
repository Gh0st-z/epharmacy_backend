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

        pharmacy_id = request.data.get('pharmacy')
        data['pharmacy'] = pharmacy_id
        product_image = request.FILES.get('product_image')

        if product_image:
            data['product_image'] = product_image

        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetProductAPI(APIView):
    def get(self, request, *args, **kwargs):
        pharmacy_id = request.GET.get('pharmacy', None)
        products = Product.objects.filter(pharmacy=pharmacy_id, product_type='product')

        if products.exists():
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


class GetMedicineAPI(APIView):
    def get(self, request, *args, **kwargs):
        pharmacy_id = request.GET.get('pharmacy', None)
        medicines = Product.objects.filter(pharmacy=pharmacy_id, product_type='medicine')

        if medicines.exists():
            serializer = ProductSerializer(medicines, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


class GetProductUpdateDetailAPI(APIView):
    def get(self, request, id, *args, **kwargs):
        products = Product.objects.filter(product_id=id)

        if products.exists():
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


class GetMedicineUpdateDetailAPI(APIView):
    def get(self, request, id, *args, **kwargs):
        medicine = Product.objects.filter(product_id=id, product_type='medicine')

        if medicine.exists():
            serializer = ProductSerializer(medicine, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


class UpdateProductAPI(APIView):
    def put(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id', None)
        product = Product.objects.filter(product_id=product_id)

        data = {
            'product_name': request.data.get('product_name', product.product_name),
            'product_info': request.data.get('product_info', product.product_info),
            'price': request.data.get('price', product.price),
            'product_type': request.data.get('product_type', product.product_type),
            'quantity': request.data.get('quantity', product.quantity),
        }

        serialzer = ProductSerializer(product, data=data)
        if serialzer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


class UpdateMedicineAPI(APIView):
    def put(self, request, *args, **kwargs):
        medicine_id = request.GET.get('product_id', None)
        medicine = Product.objects.filter(product_id=product_id)

        data = {
            'product_name': request.data.get('product_name', product.product_name),
            'product_info': request.data.get('product_info', product.product_info),
            'price': request.data.get('price', product.price),
            'product_type': request.data.get('product_type', product.product_type),
            'quantity': request.data.get('quantity', product.quantity),
        }

        serialzer = ProductSerializer(medicine, data=data)
        if serialzer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)
