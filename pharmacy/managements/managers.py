from autho.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class PharmacyManager(BaseUserManager):
    def _create_pharmacy(self, pharmacy_name, address, license_number, phone_number, pharmacy_type, pharmacy_logo, website_url, admin_id):
        pharmacy_name = self.normalize_email(pharmacy_name)
        pharmacy = self.model(
            address=address,
            license_number=license_number,
            phone_number=phone_number,
            pharmacy_type=pharmacy_type,
            pharmacy_logo=pharmacy_logo,
            website_url=website_url,
            admin_id=admin_id
        )
        pharmacy.save(using=self._db)
        return pharmacy

    def create_pharmacy(self, pharmacy_name, address, license_number, phone_number, pharmacy_type, pharmacy_logo, website_url, admin_id):
        return self._create_pharmacy(
            pharmacy_name=pharmacy_name,
            address=address,
            license_number=license_number,
            phone_number=phone_number,
            pharmacy_type=pharmacy_type,
            pharmacy_logo=pharmacy_logo,
            website_url=website_url,
            admin_id=admin_id
        )
