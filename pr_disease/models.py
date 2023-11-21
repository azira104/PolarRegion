from django.db import models

# Create your models here.

class birdInfluenza_bELISA(models.Model):
    id = models.AutoField(primary_key=True)
    lab_ID = models.CharField(max_length=50)
    field_ID = models.CharField(max_length=100)
    host_species = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    sampling_date = models.DateField()
    location = models.CharField(max_length=255)
    location_notes = models.TextField()
    lat = models.FloatField()
    long = models.FloatField()
    test_date = models.DateField()
    sample_ABS = models.FloatField()
    neg_ctrl = models.FloatField()
    S_N_ratio = models.FloatField()
    result = models.CharField(max_length=10)
    replicate = models.IntegerField()

    def __str__(self):
        return self.host_species
    
class birdInfluenza_HI(models.Model):
    id = models.AutoField(primary_key=True)
    lab_ID = models.CharField(max_length=50)
    host_species = models.CharField(max_length=255)
    H1N2 = models.CharField(max_length=10)
    H2N2 = models.CharField(max_length=10)
    H3N2 = models.CharField(max_length=10)
    H4N2 = models.CharField(max_length=10)
    H5N2 = models.CharField(max_length=10)
    H6N2 = models.CharField(max_length=10)
    H7N3 = models.CharField(max_length=10)
    H8N4 = models.CharField(max_length=10)
    H9N2 = models.CharField(max_length=10)
    H10N2 = models.CharField(max_length=10)
    H11N2 = models.CharField(max_length=10)
    H12N2 = models.CharField(max_length=10)
    H13N6 = models.CharField(max_length=10)
    H14N2 = models.CharField(max_length=10)
    H16N3 = models.CharField(max_length=10)
    HI_result = models.CharField(max_length=10)

    def __str__(self):
        return self.host_species

class wildlife_cysts_oocysts(models.Model):
    id = models.AutoField(primary_key=True)
    field_ID = models.CharField(max_length=20)
    lab_ID = models.CharField(max_length=20)
    species = models.CharField(max_length=100)
    common_name = models.CharField(max_length=20)
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    age_class = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    cryptosporidium = models.CharField(max_length=10)
    giardia = models.CharField(max_length=10)

    def __str__(self):
        return self.common_name 