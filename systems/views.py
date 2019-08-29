from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .searializers import WarehouseSerializer



@api_view(['GET', 'POST'])
def warehouse_list(request):

    if request.method == 'GET':
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(type(request.data))
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def pond_list(request):

    if request.method == 'GET':
        ponds = Pond.objects.all()
        serializer = PondSerializer(ponds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(type(request.data))
        serializer = PondSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def plant_list(request):

    if request.method == 'GET':
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(type(request.data))
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Detailed APIs

@api_view(['GET', 'POST'])
def plant_list(request, pid):

    if request.method == 'GET':

        requested = request.data
        plantID = pid

        plants = Plant.objects.filter(id=plantID)[0]
        data = {}

        data['id'] = plants.id
        data['planted'] = plants.planted
        data['name'] = plants.name
        data['type'] = plants.plantType

        wh = plants.Warehouse.id
        plantWarehouse = Warehouse.objects.filter(id = wh)
        plantWarehouse = plantWarehouse[0]
        own = plantWarehouse.owner
        data['username'] = own.username
        data['warehouse'] = plantWarehouse.name
        data['zip'] = plantWarehouse.zipCode

        plantPond = Pond.objects.filter(Warehouse = plants.Warehouse)[0]
        data['pond'] = plantPond.name

        conditions = {}

        data['conditions'] = 'available in the next update'

        return Response(data)



        # serializer = PlantSerializer(plants, many=True)
        # return Response(serializer.data)

    elif request.method == 'POST':
        # print(type(request.data))
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
