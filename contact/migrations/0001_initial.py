# Generated by Django 3.2 on 2023-01-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('name', models.CharField(max_length=50)),
                ('buy_sell', models.CharField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')], default=None, max_length=20)),
                ('phone_nr', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
