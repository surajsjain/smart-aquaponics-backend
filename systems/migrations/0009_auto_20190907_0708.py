# Generated by Django 2.2.4 on 2019-09-07 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0008_auto_20190907_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='planted',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 7, 8, 28, 574173)),
        ),
    ]