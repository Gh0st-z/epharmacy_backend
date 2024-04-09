import uuid
from django.db import models

class BMI(models.Model):
    bmi_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    height = models.DecimalField(max_digits=19, decimal_places=2)
    weight = models.DecimalField(max_digits=19, decimal_places=2)
    bmi = models.DecimalField(max_digits=19, decimal_places=2)
    classification = models.CharField(max_length=255)

    objects = BMIManager()

    class Meta:
        db_table = 'bmi'

    def __str__(self):
        return str(self.bmi_id)

    @classmethod
    @transaction.atomic
    def generate_bmi(self, validated_data):
        bmi = bmi.objects.generate_bmi(**validated_data)
        return bmi


class SetReminder(models.Model):
    reminder_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medicine_name = models.CharField(max_length=255)
    medication_time = models.DateTimeField()
    dosage = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = ReminderManager()

    class Meta:
        db_table = 'reminder'

    def __str__(self):
        return str(self.reminder_id)


class FamilyProfile(models.Model):
    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)

    objects = ProfileManager()

    class Meta:
        db_table = 'family_profile'

    def __str__(self):
        return str(self.profile_id)


class DietConsultation(models.Model):
    diet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diet = models.CharField(max_length=255)
    diet_category = models.CharField(max_length=255)

    objects = DietManager()

    class Meta:
        db_table = 'diet'

    def __str__(self):
        return str(self.diet_id)
