# Generated by Django 3.2.18 on 2023-05-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('productId', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('productId', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shoese',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('productId', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
    ]
