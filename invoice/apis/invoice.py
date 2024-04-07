from autho.models import *
from order.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class Invoice(BaseUserManager):
    def _generate_invoice(self, customer_name, quantity, total_price, billing_address, customer, order):
        invoice = self.model(
            customer_name=customer_name,
            quantity = quantity,
            total_price=total_price,
            billing_address=billing_address,
            customer=customer,
            order=order,
        )
        invoice.save(using=self._db)
        return invoice

    def generate_invoice(self, **kwargs):
        return self._generate_invoice(**kwargs)
