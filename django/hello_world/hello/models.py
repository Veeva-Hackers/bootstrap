from django.db import models

class Restaurant(models.Model):
    activity_date = models.CharField(max_length=30)
    resource_code = models.CharField(max_length=30)
    human_address = models.CharField(max_length=30)
    facility_name = models.CharField(max_length=30)
    violation_description = models.CharField(max_length=30)


