# Generated by Django 2.2.4 on 2019-09-07 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0009_auto_20190907_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='planted',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 11, 28, 38, 419781)),
        ),
    ]