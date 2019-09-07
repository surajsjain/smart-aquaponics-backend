# Generated by Django 2.2.4 on 2019-09-07 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0010_auto_20190907_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishfeeding',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 12, 32, 12, 124172)),
        ),
        migrations.AlterField(
            model_name='plantconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 12, 32, 12, 122907)),
        ),
        migrations.AlterField(
            model_name='pondconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 12, 32, 12, 123375)),
        ),
        migrations.AlterField(
            model_name='watering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 12, 32, 12, 123741)),
        ),
    ]