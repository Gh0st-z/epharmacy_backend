from rest_framework import serializers
from invoice.models import *

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields = ('cart_id', 'quantity', 'price', 'total_price', 'prescription', 'customer', 'product')
        extra_kwargs={
            'prescription': {'required': False, 'allow_null': True, 'default': None}
        }

    def create(self, validated_data):
        invoice = Invoice.generate_invoice(validated_data)
        return invoice

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance
