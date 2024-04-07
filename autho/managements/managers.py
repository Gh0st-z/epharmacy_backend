from autho.models.user import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, first_name, middle_name, last_name, email, phone_number, address, password, role):
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, middle_name, last_name, email, phone_number, address, password, role):
        return self._create_user(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            password=password,
            role=role,
        )

    def update_user(self, user_id, **validated_data):
        user = User.objects.get(id=user_id)
        for field, value in validated_data.items():
            setattr(user, field, value)
        user.save()
        return user
