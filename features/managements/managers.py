from features.models import *
from autho.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class BMIManager(BaseUserManager):
    def _create_bmi(self, height, weight, bmi, classification):
        bmi = self.model(
            height=height,
            weight=weight,
            bmi=bmi,
            classification=classification,
        )
        bmi.save(using=self._db)
        return bmi

    def create_bmi(self, **kwargs):
        return self._create_bmi(**kwargs)


class ReminderManager(BaseUserManager):
    def _set_reminder(self, medicine_name, medication_time, dosage, customer):
        reminder = self.model(
            medicine_name=medicine_name,
            medication_time=medication_time,
            dosage=dosage,
            customer=customer,
        )
        reminder.save(using=self._db)
        return reminder

    def set_reminder(self, **kwargs):
        return self._set_reminder(**kwargs)


class ProfileManager(BaseUserManager):
    def _create_profile(self, first_name, middle_name, last_name, relation, medication, dosage):
        profile = self.model(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            relation=relation,
            medication=mdeication,
            dosage=dosage,
        )
        profile.save(using=self._db)
        return profile

    def create_profile(self, **kwargs):
        return self._create_profile(**kwargs)


class DietManager(BaseUserManager):
    def _add_diet(self, diet, diet_category):
        diet = self.model(
            diet=diet,
            diet_category=diet_category,
        )
        diet.save(using=self._db)
        return diet

    def add_diet(self, **kwargs):
        return self._add_diet(**kwargs)
