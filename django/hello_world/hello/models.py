import io
import json
import os
from datetime import datetime
from hello_world import settings

from django.db import models

class Restaurant(models.Model):
    activity_date = models.DateTimeField()
    resource_code = models.CharField(max_length=100)
    human_address = models.CharField(max_length=300)
    facility_name = models.CharField(max_length=300)
    violation_description = models.CharField(max_length=1000)

def parseFromFlatFile():
    restaurantJsonPath = os.path.join(settings.BASE_DIR, 'static/restaurantinspect.json')
    restaurantJsonArray = json.loads(open(restaurantJsonPath).read())

    restaurants = []
    for restaurantJson in restaurantJsonArray:
        restaurant = Restaurant()
        restaurant.facility_name = restaurantJson['facility_name']
        if 'resource_code' in restaurantJson:
            restaurant.resource_code = restaurantJson['resource_code']

        restaurant.human_address = restaurantJson['location_1']['human_address']

        if 'activity_date' in restaurantJson:
            iso8601Str = restaurantJson['activity_date']
            restaurant.activity_date = datetime.strptime(iso8601Str, "%Y-%m-%dT%H:%M:%S")
        else:
            restaurant.activity_date = datetime.now()
        if 'violation_description' in restaurantJson:
            restaurant.violation_description = restaurantJson['violation_description']

        restaurants.append(restaurant)
    return restaurants

def load():
    for restaurant in parseFromFlatFile():
        restaurant.save()
