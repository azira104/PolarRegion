from django.db import models

# Create your models here.
class coral(models.Model):
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

class gentooPenguin(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=100)
    season = models.IntegerField()
    date_pair_count = models.DateField()
    total_number_pairs_with_eggs = models.IntegerField()
    total_number_of_pairs_without_eggs = models.IntegerField()
    total_number_of_pairs = models.IntegerField()
    date_chick_count = models.DateField()
    total_number_of_chicks = models.IntegerField()
    total_number_of_eggs = models.IntegerField()
    total_number_of_nests_without_eggs = models.IntegerField()
    date_fledgling_count = models.DateField()
    total_number_of_fledglings = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"{self.species} - Season: {self.season}"

class adeliePenguin(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=100)
    season = models.IntegerField()
    colony = models.CharField(max_length=100)
    date_pair_count = models.DateField()
    total_number_pairs_with_eggs = models.IntegerField()
    total_number_of_pairs_without_eggs = models.IntegerField()
    total_number_of_pairs = models.IntegerField()
    date_chick_count = models.DateField()
    total_number_of_chicks = models.IntegerField()
    total_number_of_eggs = models.IntegerField()
    total_number_of_nests_without_eggs = models.IntegerField()
    date_fledgling_count = models.DateField()
    total_number_of_fledglings = models.IntegerField()
    comments = models.TextField()
    
    def __str__(self):
        return f"{self.species} - Season: {self.season}"
    
class chinstrapPenguin(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=100)
    colony = models.CharField(max_length=100)
    season = models.IntegerField()
    date_pair_count = models.DateField()
    total_number_pairs_with_eggs = models.IntegerField()
    total_number_of_pairs_without_eggs = models.IntegerField()
    total_number_of_pairs = models.IntegerField()
    date_chick_count = models.DateField()
    total_number_of_chicks = models.IntegerField()
    total_number_of_eggs = models.IntegerField()
    total_number_of_nests_without_eggs = models.IntegerField()
    date_fledgling_count = models.DateField()
    total_number_of_fledglings = models.IntegerField()
    comments = models.TextField()
    
    def __str__(self):
        return f"{self.species} - Season: {self.season}"
    
class giantPetrelBird(models.Model):
    id = models.AutoField(primary_key=True)
    season = models.IntegerField()
    date_of_nest_count = models.DateField()
    total_number_of_nests = models.IntegerField()
    date_chick_count = models.DateField()
    total_number_of_chicks = models.IntegerField()
    comments = models.TextField()
    
    def __str__(self):
        return self.season

class krillbase(models.Model):
    id = models.AutoField(primary_key=True)
    station = models.CharField(max_length=255)
    record_type = models.CharField(max_length=100)
    number_of_stations = models.IntegerField()
    number_of_nets = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    season = models.IntegerField()
    days_from_1st_oct = models.IntegerField()
    date = models.DateField()
    date_accuracy = models.CharField(max_length=100)
    net_time = models.TimeField()
    gmt_or_local = models.CharField(max_length=100)
    day_night = models.CharField(max_length=100)
    day_night_method = models.IntegerField()
    net_type = models.CharField(max_length=255)
    mouth_area_of_net_m2 = models.FloatField()
    top_sampling_depth_m = models.FloatField()
    bottom_sampling_depth_m = models.FloatField()
    volume_filtered_m3 = models.FloatField()
    n_or_s_polar_front = models.CharField(max_length=100)
    water_dep_mean_within_10km = models.FloatField()
    water_depth_range_within_10km = models.FloatField()
    climatological_temperature = models.FloatField()
    number_of_krill_under_1m2 = models.FloatField()
    standardised_krill_under_1m2 = models.FloatField()
    number_of_salps_under_1m2 = models.FloatField()
    
    def __str__(self):
        return self.station

class bearBlood(models.Model):
    BearID = models.IntegerField(primary_key=True)
    datetimeUTC = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    ambient_temp = models.FloatField()
    duration = models.FloatField()
    sex = models.CharField(max_length=10)
    mass = models.FloatField()
    measuredTelazol_dose = models.FloatField()
    ALT = models.FloatField()
    Glucose = models.FloatField()
    Sodium = models.FloatField()
    Potassium = models.FloatField()
    WBC_count = models.FloatField()
    Lymphocyte = models.FloatField()
    Neutrophil = models.FloatField()
    Cortisol = models.FloatField()
    Glutamic_acid = models.FloatField()

class bearAbdominalTemp(models.Model):
    BearID = models.IntegerField(primary_key=True)
    datetimeUTC = models.DateTimeField()
    bodyTemp_abdominal = models.FloatField()
    
class bearActivity(models.Model):
    BearID = models.IntegerField(primary_key=True)
    datetimeUTC = models.DateTimeField()
    Activity_count = models.IntegerField()
    
class bearPeripheralTemp(models.Model):
    BearID = models.IntegerField(primary_key=True)
    datetimeUTC = models.DateTimeField()
    bodyTemp_peripheral = models.FloatField()
    
class bearCapSequence(models.Model):
    BearID = models.IntegerField(primary_key=True)
    datetimeUTC = models.DateTimeField()
    Event = models.CharField(max_length=100)
    Rectal_temp = models.FloatField()