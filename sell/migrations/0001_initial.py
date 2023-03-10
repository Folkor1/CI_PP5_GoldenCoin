# Generated by Django 3.2 on 2023-01-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70, null=True)),
                ('coin_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('metal', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=100)),
                ('ask_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('negotiable', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Sell',
            },
        ),
    ]
