from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from autho.models.user import User
from pharmacy.models.pharmacy import Pharmacy
from autho.serializers.serializers import UserSerializer

class GetStaffDetailsAPI(APIView):
    def get(self, request, *args, **kwargs):
        staffs = User.objects.filter(role='staff')

        if staffs.exists():
            serializer = UserSerializer(staffs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


class GetUserUpdateDetailAPI(APIView):
    def get(self, request, id, *args, **kwargs):
        user = User.objects.filter(id=id)
        if user.exists():
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


class GetAllUserDetailAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        if user.exists():
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No data found!'}, status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class LoginUserAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
        }

        try:
            user_login = User.objects.get(email=data['email'])
            user_data = UserSerializer(user_login).data
        except User.DoesNotExist:
            return Response({'Error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(data['password'], user_login.password) and user_login.role == "customer":
            user = authenticate(request, **data)
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response(
                    {'refresh': str(refresh), 'access': str(refresh.access_token), **user_data},
                    status=status.HTTP_200_OK
                )

        if check_password(data['password'], user_login.password) and user_login.role == "admin":
            user = authenticate(request, **data)
            if user is not None:
                try:
                    pharmacy = Pharmacy.objects.get(admin_id=user_login.id)
                    if pharmacy:
                        login(request, user)
                        user_data['pharmacy_exists'] = 'True'
                        user_data['pharmacy_id'] = pharmacy.pharmacy_id
                        refresh = RefreshToken.for_user(user)
                        return Response(
                            {'refresh': str(refresh), 'access': str(refresh.access_token), **user_data},
                            status=status.HTTP_200_OK
                        )
                except Pharmacy.DoesNotExist:
                    login(request, user)
                    user_data['pharmacy_exists'] = 'False'
                    return Response(
                        {'refresh': str(refresh), 'access': str(refresh.access_token), **user_data},
                        status=status.HTTP_200_OK
                    )

        return Response({'Error': 'Login not succeeded!'}, status=status.HTTP_401_UNAUTHORIZED)
