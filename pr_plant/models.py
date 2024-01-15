from django.db import models

# Create your models here.

class microbialSymbionts(models.Model):
    id = models.AutoField(primary_key=True)
    plant = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
    response_unit = models.CharField(max_length=255)
    mean = models.CharField(max_length=255)
    n = models.FloatField()
    dispersion_value = models.IntegerField()
    dispersion_measure = models.FloatField()
    cold_condition = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    infection_status = models.CharField(max_length=10)
    microorganism = models.CharField(max_length=255)
    comment = models.TextField()
    
    def __str__(self):
        return self.plant
    
class glacierAlgae(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10)
    f = models.IntegerField()
    fm = models.IntegerField()
    par = models.IntegerField()
    y = models.FloatField()
    etr = models.FloatField()
    rep = models.CharField(max_length=10)
    treat = models.CharField(max_length=50)
    npq = models.FloatField()
    etrmax = models.FloatField()
    alpha = models.FloatField()
    ek = models.FloatField()

    def __str__(self):
        return self.type