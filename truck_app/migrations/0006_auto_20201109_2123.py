# Generated by Django 3.1.3 on 2020-11-09 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck_app', '0005_auto_20201108_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': [('d', 'i')]},
        ),
    ]
