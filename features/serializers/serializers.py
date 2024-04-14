from rest_framework import serializers
from features.models import *

class BMISerializer(serializers.ModelSerializer):
    class Meta:
        model=BMI
        fields = ('bmi_id', 'height', 'weight', 'bmi', 'classification')

    def create(self, validated_data):
        bmi = BMI.create_bmi(validated_data)
        return bmi


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model=SetReminder
        fields = ('reminder_id', 'medicine_name', 'medication_time', 'dosage', 'customer')

    def create(self, validated_data):
        reminder = SetReminder.set_reminder(validated_data)
        return reminder


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=FamilyProfile
        fields = ('profile_id', 'first_name', 'middle_name', 'last_name', 'relation', 'medication', 'dosage')

    def create(self, validated_data):
        profile = FamilyProfile.create_profile(validated_data)
        return profile


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model=('diet_id', 'diet', 'diet_category')

    def create(self, validated_data):
        diet = DietConsultation.add_diet(validated_data)
        return diet
