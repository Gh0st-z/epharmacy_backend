from rest_framework import serializers
from pharmacy.models import *

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model=Pharmacy
        fields = ('pharmacy_name', 'address', 'license_number', 'phone_number', 'pharmacy_type', 'pharmacy_logo', 'website_url', 'admin_id')
        extra_kwargs = {
            'pharmacy_logo': {'required': False, 'allow_null': True, 'default': None}
        }

    def create(self, validated_data):
        pharmacy = Pharmacy.create_pharmacy(validated_data)
        return pharmacy

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance
