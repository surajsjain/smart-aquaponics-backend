# Generated by Django 2.2.4 on 2019-09-07 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0011_auto_20190907_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuatoroverride',
            name='manual',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='fishfeeding',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 14, 22, 14, 895781)),
        ),
        migrations.AlterField(
            model_name='plantconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 14, 22, 14, 894605)),
        ),
        migrations.AlterField(
            model_name='pondconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 14, 22, 14, 895001)),
        ),
        migrations.AlterField(
            model_name='watering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 14, 22, 14, 895370)),
        ),
    ]