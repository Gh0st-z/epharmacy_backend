from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from autho.models import User
from product.models import Product
from order.managements.cart import CartManager
import uuid

class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    total_price = models.DecimalField(max_digits=19, decimal_places=2)
    prescription = models.ImageField(upload_to='uploads/', null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    objects=CartManager()

    class Meta:
        db_table='cart'

    def __str__(self):
        return str(self.cart_id)

    @classmethod
    @transaction.atomic
    def create_cart(self, validated_data):
        cart = Cart.objects.create_cart(**validated_data)
        return cart
