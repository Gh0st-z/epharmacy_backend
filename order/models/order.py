from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from autho.models import User
from order.models import Cart
from order.managements.order import OrderManager
import uuid

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    total_price = models.DecimalField(max_digits=19, decimal_places=2)
    billing_address = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    objects=OrderManager()

    class Meta:
        db_table='order'

    def __str__(self):
        return str(self.cart_id)

    @classmethod
    @transaction.atomic
    def create_order(self, validated_data):
        order = Order.objects.create_order(**validated_data)
        return order
