# Generated by Django 5.1.7 on 2025-06-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('tenant', 'Tenant'), ('landlord', 'Landlord')], max_length=10),
        ),
    ]
