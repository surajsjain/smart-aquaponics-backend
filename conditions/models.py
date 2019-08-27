from django.db import models
from systems.models import *
from datetime import datetime

# Create your models here.

class PlantConditions(models.Model):
    timestamp = models.DateTimeField(default = datetime.now())
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    temperature = models.FloatField()
    humidity = models.FloatField()
    soilMoisture = models.FloatField()

    diseased = models.BooleanField(default=False)

class PondConditions(models.Model):
    timestamp = models.DateTimeField(default = datetime.now())
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)

    level = models.FloatField()
    purity = models.FloatField(default=True)

class Watering(models.Model):
    timestamp = models.DateTimeField(default = datetime.now())

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)

    quantity = models.FloatField()
