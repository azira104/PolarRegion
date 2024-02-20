from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv

# calling from models.py
from .models import antarcticMass, antarcticHotpoints

# Create your views here.
def AntarcticaRoutes(request):
    return render(request, 'AntarcticaRoutes.html')

def antartic1(request):
    return render(request, 'antartic1.html')

def antartic2(request):
    return render(request, 'antartic2.html')

def antarticmass(request):
    antarticmass_data = antarcticMass.objects.all()
    return render(request, 'antarticmass.html', {'antarticmass': antarticmass_data})

def hotpoints(request):
    hotpoints_data = antarcticHotpoints.objects.all()
    return render(request, 'hotpoints.html', {'hotpoints': hotpoints_data})
def iceradar(request):
    return render(request, 'iceradar.html')
def snow(request):
    return render(request, 'snow.html')

# def download_antarctic_mass_csv(request):
#     antarctic_mass_data = antarcticMass.objects.all()

#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="antarctic_mass.csv"'

#     writer = csv.writer(response)

#     # Write header row
#     writer.writerow(['Year', 'Antarctic Mass', 'Uncertainty'])

#     # Write data rows
#     for item in antarctic_mass_data:
#         writer.writerow([item.year, item.antarctic_mass, item.antarcticMass_1sigma_uncertainty])

#     return response

# def download_antarctic_hotpoints_csv(request):
#     hotpoints_data = antarcticHotpoints.objects.all()
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="antarctic_hotpoints_data.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['Latitude', 'Longitude', 'Brightness', 'Scan', 'Track', 'Acquisition Date', 'Acquisition Time', 'Satellite', 'Confidence', 'Bright T31', 'FRP', 'Type'])
#     for data in hotpoints_data:
#         writer.writerow([data.latitude, data.longitude, data.brightness, data.scan, data.track, data.acq_date, data.acq_time, data.satellite, data.confidence, data.bright_t31, data.frp, data.type])
#     return response