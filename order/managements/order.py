from autho.models import *
from order.models import Cart
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class OrderManager(BaseUserManager):
    def _create_order(self, quantity, price, total_price, billing_address, status, customer, cart):
        order = self.model(
            quantity = quantity,
            price=price,
            total_price=total_price,
            billing_address=billing_address,
            status=status,
            customer=customer,
            cart=cart,
        )
        order.save(using=self._db)
        return order

    def create_order(self, **kwargs):
        return self._create_order(**kwargs)
