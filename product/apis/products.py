from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from uuid import UUID
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
    def put(self, request, id, *args, **kwargs):
        product_id = id

        try:
            product = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'product_name': request.data.get('product_name', product.product_name),
            'product_info': request.data.get('product_info', product.product_info),
            'price': request.data.get('price', product.price),
            'product_type': 'product',
            'quantity': request.data.get('quantity', product.quantity),
        }

        product_image = request.FILES.get('product_image')

        if product_image:
            data['product_image'] = product_image

        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateMedicineAPI(APIView):
    def put(self, request, id, *args, **kwargs):
        product_id = id

        try:
            medicine = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'product_name': request.data.get('product_name', medicine.product_name),
            'product_info': request.data.get('product_info', medicine.product_info),
            'price': request.data.get('price', medicine.price),
            'product_type': 'medicine',
            'quantity': request.data.get('quantity', medicine.quantity),
        }

        product_image = request.FILES.get('product_image')

        if product_image:
            data['product_image'] = product_image

        serializer = ProductSerializer(medicine, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProductAPI(APIView):
    def delete(self, request, id, *args, **kwargs):
        product_id = id

        try:
            product = Product.objects.get(product_id=id)
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({'message': 'Product has been deleted'}, status=status.HTTP_200_OK)
