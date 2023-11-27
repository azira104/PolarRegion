from django.db import models

# Create your models here.

class antarcticMass(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    antarctic_mass = models.FloatField()
    antarcticMass_1sigma_uncertainty = models.FloatField()

    def __str__(self):
        return self.year
    
class antarcticHotpoints(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    brightness = models.FloatField()
    scan = models.FloatField()
    track = models.FloatField()
    acq_date = models.DateField()
    acq_time = models.IntegerField()
    satellite = models.CharField(max_length=5)
    confidence = models.CharField(max_length=5)
    bright_t31 = models.FloatField()
    frp = models.FloatField()
    type = models.IntegerField()

    def __str__(self):
        return self.type