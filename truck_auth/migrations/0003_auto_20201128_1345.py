# Generated by Django 3.1.3 on 2020-11-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_auth', '0002_auto_20201128_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
