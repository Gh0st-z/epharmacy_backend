# Generated by Django 4.2.8 on 2024-05-13 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('pharmacy_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pharmacy_name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('license_number', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('pharmacy_type', models.CharField(max_length=100)),
                ('pharmacy_logo', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('website_url', models.CharField(blank=True, max_length=100, null=True)),
                ('admin_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pharmacy',
            },
        ),
    ]
