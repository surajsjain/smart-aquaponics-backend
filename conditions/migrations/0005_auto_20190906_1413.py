# Generated by Django 2.2.4 on 2019-09-06 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0004_auto_20190903_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishfeeding',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 14, 13, 53, 342306)),
        ),
        migrations.AlterField(
            model_name='plantconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 14, 13, 53, 341151)),
        ),
        migrations.AlterField(
            model_name='pondconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 14, 13, 53, 341550)),
        ),
        migrations.AlterField(
            model_name='watering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 14, 13, 53, 341907)),
        ),
    ]
