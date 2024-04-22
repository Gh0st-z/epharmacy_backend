from django.urls import path
from autho.apis.registration import *
from autho.apis.user import *

urlpatterns = [
    path('register-get/', CheckRegsiteredEmailAPI.as_view(), name='register-get'),
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('login/', LoginUserAPI.as_view(), name='login'),
    path('get-staff/', GetStaffDetailsAPI.as_view(), name='get-staff'),
    path('user-list/', GetAllUserDetailAPI.as_view(), name='user-list'),
    path('get-user/<uuid:id>/', GetUserUpdateDetailAPI.as_view(), name='get-user'),
    path('update-user/<uuid:id>/', UpdateUserAPI.as_view(), name='update-user'),
]
