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
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    year = models.IntegerField()
    hemisphere = models.CharField(max_length=50)
    average_temperature = models.FloatField()
    east_west = models.CharField(max_length=10)

    def __str__(self):
        return self.country
    
class alaskaStreamgages(models.Model):
    id = models.AutoField(primary_key=True)
    agency = models.CharField(max_length=10)
    location_id = models.IntegerField()
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    lat_long_type = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    hydrologic_unit = models.IntegerField()
    drainage_area = models.FloatField()
    datum_of_page = models.FloatField()
    datum_type = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class simpsonLagoon(models.Model):
    id = models.AutoField(primary_key=True)
    sample_ID = models.CharField(max_length=10)
    type = models.CharField(max_length=100)
    volume = models.FloatField()
    mid_sampling = models.DateTimeField()
    season = models.CharField(max_length=100)
    year = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    salinity = models.FloatField()
    temperature = models.FloatField()
    radium224 = models.FloatField()
    error224 = models.FloatField()
    radium223 = models.FloatField()
    error223 = models.FloatField()
    radium228 = models.FloatField()
    error228 = models.FloatField()
    radium226 = models.FloatField()
    error226 = models.FloatField()

    def __str__(self):
        return self.season