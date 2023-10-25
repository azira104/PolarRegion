from django.db import models

# Create your models here.
class sulfur(models.Model):
    
    #year, neem, wdc double in mysql
    year = models.FloatField()
    neem = models.FloatField()
    wdc = models.FloatField()    

    def __str__(self):
        return self.name