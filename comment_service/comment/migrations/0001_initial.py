# Generated by Django 2.2.14 on 2023-03-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('productId', models.CharField(max_length=10)),
                ('comment', models.CharField(max_length=255)),
            ],
        ),
    ]
