from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from pharmacy.models import Pharmacy
from autho.models import User
from pharmacy.serializers.serializers import PharmacySerializer

class CreatePharmacyProfileAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'pharmacy_name': request.data.get('pharmacy_name'),
            'address': request.data.get('address'),
            'license_number': request.data.get('license_number'),
            'phone_number': request.data.get('phone_number'),
            'pharmacy_type': request.data.get('pharmacy_type'),
            'website_url': request.data.get('website_url'),
        }
        admin_id = request.data.get('admin_id')
        data['admin_id'] = admin_id
        pharmacy_logo = request.FILES.get('pharmacy_logo')

        if pharmacy_logo:
            data['pharmacy_logo'] = pharmacy_logo
            
        serializer = PharmacySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetPharmacyProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        pharmacy_name = request.GET.get('pharmacy_name', None)
        pharmacy = Pharmacy.objects.filter(pharmacy_name=pharmacy_name)
        if pharmacy.exists():
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})
