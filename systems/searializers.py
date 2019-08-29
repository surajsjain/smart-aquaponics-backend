from rest_framework import serializers
from .models import *

class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'

class PondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pond
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = '__all__'
