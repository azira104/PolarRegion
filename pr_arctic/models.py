from django.db import models

# Create your models here.

class iceExtent(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    extent = models.FloatField()

    def __str__(self):
        return self.year

class g(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salinity = models.FloatField()
    january_temp = models.FloatField()
    june_temp = models.FloatField()
    area = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    type_of_sea = models.FloatField()
    silt_sulfide = models.FloatField()
    coral_status = models.FloatField()

    def __str__(self):
        return self.name