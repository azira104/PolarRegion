from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv

# calling from models.py
from .models import penguinPopulation, penguinIter, penguinSize

# Create your views here.
def mfungi(request):
    return render(request, 'mfungi.html')

def penguinpopu(request):
    penguinpopu_data = penguinPopulation.objects.all()
    return render(request, 'penguinpopu.html', {'penguinpopu': penguinpopu_data})

def palmerIter(request):
    palmerIter_data = penguinIter.objects.all()
    return render(request, 'palmerIter.html', {'palmerIter': palmerIter_data})

def palmerSize(request):
    palmerSize_data = penguinSize.objects.all()
    return render(request, 'palmerSize.html', {'palmerSize': palmerSize_data})

def download_penguin_population_csv(request):
    # Query data from MySQL
    population_data = penguinPopulation.objects.all()

    # Define CSV header and rows
    csv_header = ['Site Name', 'Site ID', 'CCAMLR Region', 'Longitude', 'Latitude', 'Common Name', 'Day', 'Month', 'Year', 'Season Starting', 'Count', 'Accuracy', 'Count Type', 'Vantage']
    csv_rows = [[p.site_name, p.site_ID, p.ccamlr_region, p.longitude, p.latitude, p.common_name, p.day, p.month, p.year, p.season_starting, p.count, p.accuracy, p.count_type, p.vantage] for p in population_data]

    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="penguin_population_data.csv"'

    # Write CSV content
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

    return response