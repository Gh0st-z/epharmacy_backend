from django.db import models, transaction
from pharmacy.models import Pharmacy
from product.managements.managers import ProductManager
import uuid

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    product_info = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    quantity = models.IntegerField()
    product_type = models.CharField(max_length=11)
    product_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    objects = ProductManager()
    USERNAME_FIELD = 'product_name'

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.id)

    @classmethod
    @transaction.atomic
    def create_product(self, validated_data):
        product = Product.objects.create_product(**validated_data)
        return product
