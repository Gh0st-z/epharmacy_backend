from rest_framework import serializers
from order.models import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = ('cart_id', 'quantity', 'price', 'total_price', 'prescription', 'customer', 'product')
        extra_kwargs={
            'prescription': {'required': False, 'allow_null': True, 'default': None}
        }

    def create(self, validated_data):
        cart = Cart.create_cart(validated_data)
        return user

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = ('order_id', 'quantity', 'price', 'total_price', 'billing_address', 'status', 'customer', 'cart')

    def create(self, validated_data):
        order = Order.create_order(validated_data)
        return order

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance
