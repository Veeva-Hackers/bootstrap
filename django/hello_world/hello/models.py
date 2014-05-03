import io
import json
import os
from datetime import datetime
from hello_world import settings

from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)

class Restaurant(models.Model):
    activity_date = models.DateTimeField()
    resource_code = models.CharField(max_length=100)
    human_address = models.CharField(max_length=300)
    facility_name = models.CharField(max_length=300, primary_key=True)
    violation_description = models.CharField(max_length=1000)

    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    location_1 = models.OneToOneField(Address, null=True)

def load():
    restaurant_json_path = os.path.join(settings.BASE_DIR, 'static/restaurantinspect.json')
    restaurant_json_array = json.loads(open(restaurant_json_path).read())

    for restaurantJson in restaurant_json_array:
        restaurant = Restaurant()
        restaurant.facility_name = restaurantJson['facility_name']
        if 'resource_code' in restaurantJson:
            restaurant.resource_code = restaurantJson['resource_code']

        if 'location_1' in restaurantJson:
            location_json = restaurantJson['location_1']
            restaurant.longitude = location_json['longitude']
            restaurant.latitude = location_json['latitude']
            restaurant.human_address = location_json['human_address']

            address_json = json.loads(restaurant.human_address)

            address = Address()
            address.address = address_json['address']
            address.city = address_json['city']
            address.state = address_json['state']
            address.zip = address_json['zip']
            address.save()

            restaurant.location_1 = address

        if 'activity_date' in restaurantJson:
            iso_string = restaurantJson['activity_date']
            restaurant.activity_date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S")
        else:
            restaurant.activity_date = datetime.now()
        if 'violation_description' in restaurantJson:
            restaurant.violation_description = restaurantJson['violation_description']

        restaurant.save()
