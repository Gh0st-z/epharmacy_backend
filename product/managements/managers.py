from pharmacy.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class ProductManager(BaseUserManager):
    def _create_product(self, product_name, product_info, price, quantity, product_type, product_image, pharmacy):
        product = self.model(
            product_name=product_name,
            product_info=product_info,
            price=price,
            quantity=quantity,
            product_type=product_type,
            product_image=product_image,
            pharmacy=pharmacy
        )
        product.save(using=self._db)
        return product

    def create_product(self, product_name, product_info, price, quantity, product_type, product_image, pharmacy):
        return self._create_product(
            product_name=product_name,
            product_info=product_info,
            price=price,
            quantity=quantity,
            product_type=product_type,
            product_image=product_image,
            pharmacy=pharmacy
        )
