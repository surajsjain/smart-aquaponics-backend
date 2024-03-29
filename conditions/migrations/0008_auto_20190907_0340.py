# Generated by Django 2.2.4 on 2019-09-07 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0007_auto_20190906_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishfeeding',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 3, 40, 3, 608924)),
        ),
        migrations.AlterField(
            model_name='plantconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 3, 40, 3, 607713)),
        ),
        migrations.AlterField(
            model_name='pondconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 3, 40, 3, 608116)),
        ),
        migrations.AlterField(
            model_name='watering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 3, 40, 3, 608510)),
        ),
    ]
