from autho.models import *
from product.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class CartManager(BaseUserManager):
    def _create_cart(self, quantity, price, total_price, prescription, customer, product):
        cart = self.model(
            quantity = quantity,
            price=price,
            total_price=total_price,
            prescription=prescription,
            customer=customer,
            product=product,
        )
        cart.save(using=self._db)
        return cart

    def create_cart(self, **kwargs):
        return self._create_cart(**kwargs)
