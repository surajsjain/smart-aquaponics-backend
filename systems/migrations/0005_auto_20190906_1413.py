# Generated by Django 2.2.4 on 2019-09-06 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0004_auto_20190903_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='planted',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 14, 13, 53, 340629)),
        ),
    ]
