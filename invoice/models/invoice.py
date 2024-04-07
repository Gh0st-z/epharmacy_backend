from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from autho.models import User
from order.models import Order
from invoice.managements.managers import InvoiceManager
import uuid

class Invoice(models.Model):
    invoice_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=19, decimal_places=2)
    billing_address = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    objects=InvoiceManager()

    class Meta:
        db_table='invoice'

    def __str__(self):
        return str(self.invoice_id)

    @classmethod
    @transaction.atomic
    def generate_invoice(self, validated_data):
        invoice = Invoice.objects.generate_invoice(**validated_data)
        return invoice
