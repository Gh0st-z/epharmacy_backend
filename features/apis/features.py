from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from features.models.features import *
from features.serializers.serializers import *


class CreateReminderAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'medicine_name' = request.data.get('medicine_name'),
            'medication_time' = request.data.get('medication_time'),
            'dosage' = request.data.get('dosage'),
        }

        customer_id = request.GET.get('customer')
        data['customer'] = customer_id

        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid data provided!'}, status=status.HTTP_401_UNAUTHORIZED)


class SendReminderNotificationAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        reminder_id = kwargs.get('reminder_id')
        try:
            reminder = SetReminder.objects.get(reminder_id=reminder_id)
        except SetReminder.DoesNotExist:
            return Response({'message': 'Reminder not found!'}, status=status.HTTP_400_BAD_REQUEST)
