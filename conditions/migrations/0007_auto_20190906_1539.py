# Generated by Django 2.2.4 on 2019-09-06 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0006_auto_20190906_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishfeeding',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 15, 39, 49, 251846)),
        ),
        migrations.AlterField(
            model_name='plantconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 15, 39, 49, 250533)),
        ),
        migrations.AlterField(
            model_name='pondconditions',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 15, 39, 49, 250989)),
        ),
        migrations.AlterField(
            model_name='watering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 15, 39, 49, 251426)),
        ),
    ]
