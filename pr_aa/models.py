from django.db import models

# Create your models here.
class sulfur(models.Model):
    
    #year, neem, wdc double in mysql
    id = models.AutoField(primary_key=True)
    year = models.FloatField()
    neem = models.FloatField()
    wdc = models.FloatField()    

    def __str__(self):
        return self.year