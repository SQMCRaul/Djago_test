# Generated by Django 2.1 on 2021-03-10 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='buy_date',
            field=models.DateField(default=datetime.date(2021, 3, 10)),
        ),
    ]