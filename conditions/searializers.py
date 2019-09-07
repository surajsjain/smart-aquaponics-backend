from rest_framework import serializers
from .models import *

# class WarehouseSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Warehouse
#         fields = '__all__'
#
# class PondSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Pond
#         fields = '__all__'
#
# class PlantSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Plant
#         fields = '__all__'

class PlantConditionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantConditions
        fields = ['timestamp', 'plant', 'temperature', 'humidity', 'soilMoisture', 'diseased']


class PondConditionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PondConditions
        fields = ['timestamp', 'pond', 'level', 'purity']


class WateringConditionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watering
        fields = ['timestamp', 'plant', 'pond', 'quantity']

class FishFeedingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FishFeeding
        fields = ['timestamp', 'pond']

class InFocusSerializer(serializers.ModelSerializer):

    class Meta:
        model = InFocus
        fields = ['plant', 'temperature', 'humidity', 'soilMoisture', 'diseased']
        # fields = '__all__'##['plant', 'temperature', 'humidity', 'soilMoisture', 'diseased']


class ActuatorOverrideSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActuatorOverride
        fields = ['plant', 'manual', 'water', 'light']
