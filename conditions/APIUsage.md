# API Usage

This markdown tells you everything about different APIs offered by the conditions app of speeveponics and also the get and post requests supported by them

## Urls associated with the APIs
1. __Plant Conditions:__ /conditions/plant (*GET* and *POST* the plant conditions)

## Plant Conditions
This API gives the current conditions of the plants in the system. This API supports *GET* as well as *POST*.
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
