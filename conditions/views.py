from django.shortcuts import render

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .searializers import *


@api_view(['GET', 'POST'])
def plant_list(request):

    if request.method == 'GET':
        conditions = PlantConditions.objects.all()
        serializer = PlantConditionsSerializer(conditions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(type(request.data))
        serializer = PlantConditionsSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def pond_list(request):

    if request.method == 'GET':
        conditions = PondConditions.objects.all()
        serializer = PondConditionsSerializer(conditions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(type(request.data))
        serializer = PondConditionsSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def watering_list(request):

    if request.method == 'GET':
        conditions = Watering.objects.all()
        serializer = WateringConditionsSerializer(conditions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(type(request.data))
        serializer = WateringConditionsSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
