# Generated by Django 3.2.18 on 2023-05-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_remove_paymentmodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='checkoutId',
            field=models.IntegerField(),
        ),
    ]
