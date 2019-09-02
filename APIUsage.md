# API Usage

This markdown tells you everything about different APIs offered by the conditions app of speeveponics and also the get and post requests supported by them

## Urls associated with the APIs
1. __Plant Conditions:__ /conditions/plant (*GET* and *POST* the plant conditions)
2. __Pond Conditions:__ /conditions/pond (*GET* and *POST* the plant conditions)
3. __Watering:__ /conditions/watering (*GET* and *POST* the plant conditions)

## Plant Conditions
This API gives the conditions of the plants in the system. This API supports *GET* as well as *POST*.
#### Sample GET request
/conditions/plant returns:
```
[
    {
        "timestamp": "2019-08-30T03:55:12Z",
        "plant": 1,
        "temperature": 27.0,
        "humidity": 78.0,
        "soilMoisture": 100.0,
        "diseased": false
    }
]
```
#### Sample POST request
A post to /conditions/plant will be like:
```
{
    "timestamp": "2019-08-31T18:55:12Z",
    "plant": 1,
    "temperature": 27.0,
    "humidity": 78.0,
    "diseased": false,
    "soilMoisture": 100
}
```

# Pond Conditions
This API gives the conditions of the Ponds in the system. This API supports *GET* as well as *POST*.
#### Sample GET request
/conditions/pond returns:
```
[
    {
        "timestamp": "2019-08-30T03:38:45Z",
        "pond": 1,
        "level": 100.0,
        "purity": true
    }
]
```
#### Sample POST request
A post to /conditions/pond will be like:
```
{
    "timestamp": "2019-08-31T19:15:45Z",
    "pond": 1,
    "level": 80.0,
    "purity": true
}
```

# Watering
This API gives the watering schedule along with the pond that was used for watering in the system. This API supports *GET* as well as *POST*.
#### Sample GET request
/conditions/watering returns:
```
[
    {
        "timestamp": "2019-08-30T03:57:49Z",
        "plant": 1,
        "pond": 1,
        "quantity": 1.0
    }
]
```
#### Sample POST request
A post to /conditions/watering will be like:
```
{
    "timestamp": "2019-08-31T19:24:49Z",
    "plant": 1,
    "pond": 1,
    "quantity": 0.5
}
```
