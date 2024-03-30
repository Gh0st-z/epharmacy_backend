from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from autho.models.user import User
from autho.serializers.serializers import UserSerializer

class CheckRegsiteredEmailAPI(APIView):
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email', None)
        user = User.objects.filter(email=email)

        if user.exists():
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})

class RegisterUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'middle_name': request.data.get('middle_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'phone_number': request.data.get('phone_number'),
            'address': request.data.get('address'),
            'password': request.data.get('password'),
            'role': request.data.get('role'),
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'Invalid data provided!'}, status=status.HTTP_401_UNAUTHORIZED)
