# Generated by Django 3.2.18 on 2023-05-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutModel',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('cartIds', models.JSONField(max_length=10)),
                ('totalPrice', models.CharField(max_length=10)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
