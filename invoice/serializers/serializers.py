from rest_framework import serializers
from invoice.models import *

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields = ('invoice_id', 'customer_name', 'quantity', 'total_price', 'billing_address', 'customer', 'order')

    def create(self, validated_data):
        invoice = Invoice.generate_invoice(validated_data)
        return invoice

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance
