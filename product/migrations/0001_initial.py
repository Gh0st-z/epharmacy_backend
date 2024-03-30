# Generated by Django 4.2.8 on 2024-03-30 18:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_info', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('quantity', models.IntegerField()),
                ('product_type', models.CharField(max_length=11)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacy')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
