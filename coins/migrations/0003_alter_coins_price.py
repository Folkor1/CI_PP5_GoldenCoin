# Generated by Django 3.2 on 2023-01-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]