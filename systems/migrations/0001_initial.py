# Generated by Django 2.2.4 on 2019-08-29 15:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('zipCode', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('nFishes', models.IntegerField(default=0)),
                ('Warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.Warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planted', models.DateTimeField(default=datetime.datetime(2019, 8, 29, 15, 13, 57, 927144))),
                ('name', models.CharField(max_length=200)),
                ('plantType', models.CharField(max_length=200)),
                ('Warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.Warehouse')),
                ('pond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.Pond')),
            ],
        ),
    ]
