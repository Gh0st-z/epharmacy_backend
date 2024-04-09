from features.models import *
from user.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class BMIManager(BaseUserManager):
    def _create_bmi(self, customer_name, quantity, total_price, billing_address, customer, order):
        bmi = self.model(
            customer_name=customer_name,
            quantity = quantity,
            total_price=total_price,
            billing_address=billing_address,
            customer=customer,
            order=order,
        )
        bmi.save(using=self._db)
        return bmi

    def create_bmi(self, **kwargs):
        return self._create_bmi(**kwargs)
