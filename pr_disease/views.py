from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv

# calling from models.py
from .models import birdInfluenza_bELISA, birdInfluenza_HI, wildlife_cysts_oocysts

# Create your views here.
def bELISA(request):
    bELISA_data = birdInfluenza_bELISA.objects.all()
    return render(request, 'bELISA.html', {'bELISA': bELISA_data})

def hi(request):
    hi_data = birdInfluenza_HI.objects.all()
    return render(request, 'hi.html', {'hi': hi_data})

def crypto_giardia(request):
    crypto_giardia_data = wildlife_cysts_oocysts.objects.all()
    return render(request, 'crypto_giardia.html', {'crypto_giardia': crypto_giardia_data})

def download_birdinfluenza_belisa_csv(request):
    # Query data from MySQL
    belisa_data = birdInfluenza_bELISA.objects.all()

    # Define CSV header and rows
    csv_header = ['Lab ID', 'Field ID', 'Host Species', 'Age', 'Sampling Date', 'Location', 'Location Notes', 'Latitude', 'Longitude', 'Test Date', 'Sample ABS', 'Neg Ctrl', 'S/N Ratio', 'Result', 'Replicate']
    csv_rows = [[b.lab_ID, b.field_ID, b.host_species, b.age, b.sampling_date, b.location, b.location_notes, b.lat, b.long, b.test_date, b.sample_ABS, b.neg_ctrl, b.S_N_ratio, b.result, b.replicate] for b in belisa_data]

    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="birdinfluenza_belisa_data.csv"'

    # Write CSV content
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

    return response

def download_birdinfluenza_hi_csv(request):
    hi_data = birdInfluenza_HI.objects.all()
    csv_header = ['Lab ID', 'Host Species', 'H1N2', 'H2N2', 'H3N2', 'H4N2', 'H5N2', 'H6N2', 'H7N3', 'H8N4', 'H9N2', 'H10N2', 'H11N2', 'H12N2', 'H13N6', 'H14N2', 'H16N3', 'HI Result']
    csv_rows = [[h.lab_ID, h.host_species, h.H1N2, h.H2N2, h.H3N2, h.H4N2, h.H5N2, h.H6N2, h.H7N3, h.H8N4, h.H9N2, h.H10N2, h.H11N2, h.H12N2, h.H13N6, h.H14N2, h.H16N3, h.HI_result] for h in hi_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="birdinfluenza_hi_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_wildlife_cysts_oocysts_csv(request):
    cysts_oocysts_data = wildlife_cysts_oocysts.objects.all()
    csv_header = ['Field ID', 'Lab ID', 'Species', 'Common Name', 'Date', 'Latitude', 'Longitude', 'Age Class', 'Sex', 'Cryptosporidium', 'Giardia']
    csv_rows = [[c.field_ID, c.lab_ID, c.species, c.common_name, c.date, c.latitude, c.longitude, c.age_class, c.sex, c.cryptosporidium, c.giardia] for c in cysts_oocysts_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="wildlife_cysts_oocysts_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response