# Generated by Django 2.2.4 on 2019-09-07 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0013_auto_20190907_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='planted',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 15, 8, 33, 893851)),
        ),
    ]
