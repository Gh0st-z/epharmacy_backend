from rest_framework import serializers
from product.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ('product_id', 'product_name', 'product_info', 'price', 'quantity', 'product_type', 'product_image', 'pharmacy')
        extra_kwargs = {
            'product_image': {'required': False, 'allow_null': True, 'default': None}
        }

    def create(self, validated_data):
        product = Product.create_product(validated_data)
        return product

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance
