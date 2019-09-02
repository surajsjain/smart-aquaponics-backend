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

    def __str__(self):
        return str(self.timestamp) + ' - ' + self.plant.name

class PondConditions(models.Model):
    timestamp = models.DateTimeField(default = datetime.now())
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)

    level = models.FloatField()
    purity = models.BooleanField(default=True)

    def __str__(self):
        return str(self.timestamp) + ' - ' + self.pond.name

class Watering(models.Model):
    timestamp = models.DateTimeField(default = datetime.now())

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)

    quantity = models.FloatField()

    def __str__(self):
        return str(self.timestamp) + ' - ' + self.pond.name + ' - ' + self.plant.name

class FishFeeding(models.Model):
    timestamp = models.DateTimeField(default = datetime.now())
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)
