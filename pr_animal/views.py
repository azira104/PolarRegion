from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv
# calling from models.py
from .models import coral, gentooPenguin, adeliePenguin, chinstrapPenguin, giantPetrelBird, krillbase, bearBlood, bearAbdominalTemp, bearCapSequence

# Create your views here.
def ani_coral(request):
    coral_data = coral.objects.all()
    return render(request, 'coral.html', {'coral': coral_data})

def ani_krillbase(request):
    krillbase_data = krillbase.objects.all()
    return render(request, 'krillBase.html', {'krillBase': krillbase_data})

def ani_gentoo(request):
    gentoo_data = gentooPenguin.objects.all()
    return render(request, 'gentoo.html', {'gentoo': gentoo_data})

def ani_adelie(request):
    adelie_data = adeliePenguin.objects.all()
    return render(request, 'adelie.html', {'adelie': adelie_data})

def ani_chinstrap(request):
    chinstrap_data = chinstrapPenguin.objects.all()
    return render(request, 'chinstrap.html', {'chinstrap': chinstrap_data})

def ani_bird(request):
    bird_data = giantPetrelBird.objects.all()
    return render(request, 'bird.html', {'bird': bird_data})

def ani_bearBlood(request):
    bearBlood_data = bearBlood.objects.all()
    return render(request, 'blood.html', {'blood': bearBlood_data})

def ani_bearAbdTemp(request):
    bearAbdTemp_data = bearAbdominalTemp.objects.all()
    return render(request, 'abdTemp.html', {'abdTemp': bearAbdTemp_data})

def ani_bearCapSeq(request):
    bearCapSeq_data = bearCapSequence.objects.all()
    return render(request, 'capSeq.html', {'capSeq': bearCapSeq_data})

def download_coral_csv(request):
    coral_data = coral.objects.all()
    csv_header = ['ID', 'Name', 'Salinity', 'January Temp', 'June Temp', 'Area', 'Latitude', 'Longitude', 'Type of Sea', 'Silt Sulfide', 'Coral Status']
    csv_rows = [[c.id, c.name, c.salinity, c.january_temp, c.june_temp, c.area, c.latitude, c.longitude, c.type_of_sea, c.silt_sulfide, c.coral_status] for c in coral_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="coral_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_adelie_penguin_csv(request):
    adelie_penguin_data = adeliePenguin.objects.all()
    csv_header = ['ID', 'Species', 'Season', 'Colony', 'Date Pair Count', 'Total Number Pairs with Eggs', 'Total Number of Pairs without Eggs', 'Total Number of Pairs', 'Date Chick Count', 'Total Number of Chicks', 'Total Number of Eggs', 'Total Number of Nests without Eggs', 'Date Fledgling Count', 'Total Number of Fledglings', 'Comments']
    csv_rows = [[ap.id, ap.species, ap.season, ap.colony, ap.date_pair_count, ap.total_number_pairs_with_eggs, ap.total_number_of_pairs_without_eggs, ap.total_number_of_pairs, ap.date_chick_count, ap.total_number_of_chicks, ap.total_number_of_eggs, ap.total_number_of_nests_without_eggs, ap.date_fledgling_count, ap.total_number_of_fledglings, ap.comments] for ap in adelie_penguin_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="adelie_penguin_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_gentoo_penguin_csv(request):
    gentoo_penguin_data = gentooPenguin.objects.all()
    csv_header = ['ID', 'Species', 'Season', 'Date Pair Count', 'Total Number Pairs with Eggs', 'Total Number of Pairs without Eggs', 'Total Number of Pairs', 'Date Chick Count', 'Total Number of Chicks', 'Total Number of Eggs', 'Total Number of Nests without Eggs', 'Date Fledgling Count', 'Total Number of Fledglings', 'Comments']
    csv_rows = [[gp.id, gp.species, gp.season, gp.date_pair_count, gp.total_number_pairs_with_eggs, gp.total_number_of_pairs_without_eggs, gp.total_number_of_pairs, gp.date_chick_count, gp.total_number_of_chicks, gp.total_number_of_eggs, gp.total_number_of_nests_without_eggs, gp.date_fledgling_count, gp.total_number_of_fledglings, gp.comments] for gp in gentoo_penguin_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gentoo_penguin_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_chinstrap_penguin_csv(request):
    chinstrap_penguin_data = chinstrapPenguin.objects.all()
    csv_header = ['ID', 'Species', 'Colony', 'Season', 'Date Pair Count', 'Total Number Pairs with Eggs', 'Total Number of Pairs without Eggs', 'Total Number of Pairs', 'Date Chick Count', 'Total Number of Chicks', 'Total Number of Eggs', 'Total Number of Nests without Eggs', 'Date Fledgling Count', 'Total Number of Fledglings', 'Comments']
    csv_rows = [[cp.id, cp.species, cp.colony, cp.season, cp.date_pair_count, cp.total_number_pairs_with_eggs, cp.total_number_of_pairs_without_eggs, cp.total_number_of_pairs, cp.date_chick_count, cp.total_number_of_chicks, cp.total_number_of_eggs, cp.total_number_of_nests_without_eggs, cp.date_fledgling_count, cp.total_number_of_fledglings, cp.comments] for cp in chinstrap_penguin_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="chinstrap_penguin_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_giant_petrel_bird_csv(request):
    giant_petrel_bird_data = giantPetrelBird.objects.all()
    csv_header = ['ID', 'Season', 'Date of Nest Count', 'Total Number of Nests', 'Date Chick Count', 'Total Number of Chicks', 'Comments']
    csv_rows = [[gp.id, gp.season, gp.date_of_nest_count, gp.total_number_of_nests, gp.date_chick_count, gp.total_number_of_chicks, gp.comments] for gp in giant_petrel_bird_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="giant_petrel_bird_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_krillbase_csv(request):
    krillbase_data = krillbase.objects.all()
    csv_header = ['ID', 'Station', 'Record Type', 'Number of Stations', 'Number of Nets', 'Latitude', 'Longitude', 'Season', 'Days from 1st Oct', 'Date', 'Date Accuracy', 'Net Time', 'GMT or Local', 'Day or Night', 'Day or Night Method', 'Net Type', 'Mouth Area of Net (m2)', 'Top Sampling Depth (m)', 'Bottom Sampling Depth (m)', 'Volume Filtered (m3)', 'N or S Polar Front', 'Water Depth Mean within 10km', 'Water Depth Range within 10km', 'Climatological Temperature', 'Number of Krill under 1m2', 'Standardised Krill under 1m2', 'Number of Salps under 1m2']
    csv_rows = [[kb.id, kb.station, kb.record_type, kb.number_of_stations, kb.number_of_nets, kb.latitude, kb.longitude, kb.season, kb.days_from_1st_oct, kb.date, kb.date_accuracy, kb.net_time, kb.gmt_or_local, kb.day_night, kb.day_night_method, kb.net_type, kb.mouth_area_of_net_m2, kb.top_sampling_depth_m, kb.bottom_sampling_depth_m, kb.volume_filtered_m3, kb.n_or_s_polar_front, kb.water_dep_mean_within_10km, kb.water_depth_range_within_10km, kb.climatological_temperature, kb.number_of_krill_under_1m2, kb.standardised_krill_under_1m2, kb.number_of_salps_under_1m2] for kb in krillbase_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="krillbase_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_bear_blood_csv(request):
    bear_blood_data = bearBlood.objects.all()
    csv_header = ['ID', 'Bear ID', 'Datetime UTC', 'Latitude', 'Longitude', 'Ambient Temp', 'Duration', 'Sex', 'Mass', 'Measured Telazol Dose', 'ALT', 'Glucose', 'Sodium', 'Potassium', 'WBC Count', 'Lymphocyte', 'Neutrophil', 'Cortisol', 'Glutamic Acid']
    csv_rows = [[bb.id, bb.BearID, bb.datetimeUTC, bb.latitude, bb.longitude, bb.ambient_temp, bb.duration, bb.sex, bb.mass, bb.measuredTelazol_dose, bb.ALT, bb.Glucose, bb.Sodium, bb.Potassium, bb.WBC_count, bb.Lymphocyte, bb.Neutrophil, bb.Cortisol, bb.Glutamic_acid] for bb in bear_blood_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bear_blood_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_bear_abdominal_temp_csv(request):
    bear_abdominal_temp_data = bearAbdominalTemp.objects.all()
    csv_header = ['ID', 'Bear ID', 'Datetime UTC', 'Body Temp Abdominal']
    csv_rows = [[bat.id, bat.BearID, bat.datetimeUTC, bat.bodyTemp_abdominal] for bat in bear_abdominal_temp_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bear_abdominal_temp_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_bear_cap_sequence_csv(request):
    bear_cap_sequence_data = bearCapSequence.objects.all()
    csv_header = ['ID', 'Bear ID', 'Datetime UTC', 'Event', 'Rectal Temp']
    csv_rows = [[bcs.id, bcs.BearID, bcs.datetimeUTC, bcs.Event, bcs.Rectal_temp] for bcs in bear_cap_sequence_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bear_cap_sequence_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response