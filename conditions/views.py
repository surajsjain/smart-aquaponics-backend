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

@api_view(['GET', 'POST'])
def fishfeeding_list(request):

    if request.method == 'GET':
        conditions = FishFeeding.objects.all()
        serializer = FishFeedingSerializer(conditions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(type(request.data))
        serializer = FishFeedingSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def focus(request, pid):

    if request.method == 'GET':
        conditions = InFocus.objects.filter(id=pid)[0]
        serializer = InFocusSerializer(conditions, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':  ### WORK ON THIS
        # print(type(request.data))
        data = request.data
        ob = InFocus.objects.filter(id=pid)[0]
        ob.temperature = data["temperature"]
        ob.humidity = data["humidity"]
        ob.soilMoisture = data["soilMoisture"]
        ob.diseased = data["diseased"]

        ob.save();


        return Response(data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def actuate(request, pid):

    # if request.method == 'GET':
    #     conditions = InFocus.objects.filter(id=pid)[0]
    #     serializer = InFocusSerializer(conditions, many=False)
    #     return Response(serializer.data)

    if request.method == 'GET':
        conditions = ActuatorOverride.objects.filter(id=pid)[0]
        # data = {}
        # data["plant"] = conditions.plant.id
        # data["water"] = conditions.water
        # data["light"] = conditions.light
        #
        # print(data)
        # return Response(data)

        serializer = ActuatorOverrideSerializer(conditions, many=False)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':  ### WORK ON THIS
        # print(type(request.data))
        data = request.data
        ob = ActuatorOverride.objects.filter(id=pid)[0]

        type = data["modType"]

        if(type == "water"):
            ob.water = data["value"]

        elif(type == "light"):
            ob.light = data["value"]
        # ob.soilMoisture = data["soilMoisture"]
        # ob.diseased = data["diseased"]

        ob.save();


        return Response(data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
