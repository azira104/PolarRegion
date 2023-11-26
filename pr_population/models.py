from django.db import models

# Create your models here.

class penguinPopulation(models.Model):
    id = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=100)
    site_ID = models.CharField(max_length=10)
    ccamlr_region = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    common_name = models.CharField(max_length=100)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    season_starting = models.IntegerField()
    count = models.IntegerField()
    accuracy = models.IntegerField()
    count_type = models.CharField(max_length=10)
    vantage = models.CharField(max_length=10)

    def __str__(self):
        return self.common_name
    
class penguinSize(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=20)
    island = models.CharField(max_length=20)
    culmen_length_mm = models.FloatField()
    culmen_depth_mm = models.FloatField()
    flipper_length_mm = models.FloatField()
    body_mass_g = models.FloatField()
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.species
    
class penguinIter(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    island = models.CharField(max_length=100)
    individual_ID = models.CharField(max_length=10)
    clutch_completion = models.CharField(max_length=10)
    date_egg = models.DateField()
    culmen_length_mm = models.FloatField()
    culmen_depth_mm = models.FloatField()
    flipper_length_mm = models.FloatField()
    body_mass_g = models.FloatField()
    sex = models.CharField(max_length=10)
    delta_15_N = models.FloatField()
    delta_13_C = models.FloatField()
    comments = models.TextField()

    def __str__(self):
        return self.individual_ID