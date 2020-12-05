# Generated by Django 3.1.3 on 2020-11-28 15:03

from django.db import migrations, models
import truck_auth.validators


class Migration(migrations.Migration):

    dependencies = [
        ('truck_auth', '0004_auto_20201128_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.FloatField(blank=True, max_length=13, validators=[truck_auth.validators.validator_phone_only_numeric]),
        ),
    ]
