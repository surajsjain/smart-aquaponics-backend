from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Warehouse(models.Model):
    # warehouseUID = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # ownerUname = models.CharField(max_length=30, default=owner.username)
    name = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=20)

    def __str__(self):
        return (self.owner.username+' - '+self.name)

class Pond(models.Model):
    # pondUID = models.CharField(max_length=50)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    # warehouseUID = warehouse.warehouseUID
    name = models.CharField(max_length=40)
    nFishes = models.IntegerField(default=0)

    def __str__(self):
        return (self.Warehouse.name+' - '+self.name)

class Plant(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    planted = models.DateTimeField(default=datetime.now())
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    # warehouseUID = warehouse.warehouseUID
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)
    # pondUID = pond.pondUID
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return (self.Warehouse.name+' - '+self.name)
