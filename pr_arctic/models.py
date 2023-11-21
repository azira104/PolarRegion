from django.db import models

# Create your models here.

class iceExtent(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    extent = models.FloatField()

    def __str__(self):
        return self.year

class northernClimate(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    year = models.IntegerField()
    hemisphere = models.CharField(max_length=50)
    average_temperature = models.FloatField()
    east_west = models.CharField(max_length=10)

    def __str__(self):
        return self.city