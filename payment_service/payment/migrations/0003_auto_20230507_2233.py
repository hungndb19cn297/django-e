# Generated by Django 3.2.18 on 2023-05-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_payment_status_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('checkoutId', models.IntegerField(max_length=10)),
                ('totalPrice', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='payment_status',
        ),
    ]
