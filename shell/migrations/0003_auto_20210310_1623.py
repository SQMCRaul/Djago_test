# Generated by Django 2.1 on 2021-03-10 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0002_host_buy_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='buy_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]