from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv
from django.db import connection


# calling from models.py
from .models import iceExtent, northernClimate, alaskaStreamgages, simpsonLagoon

# Create your views here.
def climate(request):
    climate_data = northernClimate.objects.all()
    return render(request, 'climate.html', {'climate': climate_data})

def iceextent(request):
    iceextent_data = iceExtent.objects.all()
    return render(request, 'iceextent.html', {'iceextent': iceextent_data})

def simpsonlagoon(request):
    simpsonlagoon_data = simpsonLagoon.objects.all()
    return render(request, 'simpsonlagoon.html', {'simpsonlagoon': simpsonlagoon_data})

def streamgages(request):
    streamgages_data = alaskaStreamgages.objects.all()
    return render(request, 'streamgages.html', {'streamgages': streamgages_data})

def searoutes(request):
    return render(request, 'searoutes.html')

def masking(request):
    return render(request, 'masking.html')

def download_ice_extent_csv(request):
    # Query data from MySQL
    ice_extent_data = iceExtent.objects.all()

    # Define CSV header and rows
    csv_header = ['Year', 'Extent']
    csv_rows = [[str(ice.year), str(ice.extent)] for ice in ice_extent_data]

    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ice_extent_data.csv"'

    # Write CSV content
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

    return response

def download_northern_climate_csv(request):
    # Query data from MySQL
    northern_climate_data = northernClimate.objects.all()

    # Define CSV header and rows
    csv_header = ['City', 'Country', 'Latitude', 'Longitude', 'Year', 'Hemisphere', 'Average Temperature', 'East West']
    csv_rows = [[climate.city, climate.country, climate.latitude, climate.longitude, climate.year, climate.hemisphere, climate.average_temperature, climate.east_west] for climate in northern_climate_data]

    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="northern_climate_data.csv"'

    # Write CSV content
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

    return response

def download_alaska_streamgages_csv(request):
    # Query data from MySQL
    alaska_streamgages_data = alaskaStreamgages.objects.all()

    # Define CSV header and rows
    csv_header = ['Agency', 'Location ID', 'Name', 'Latitude', 'Longitude', 'Lat Long Type', 'Country', 'Hydrologic Unit', 'Drainage Area', 'Datum Of Page', 'Datum Type']
    csv_rows = [[streamgage.agency, streamgage.location_id, streamgage.name, streamgage.latitude, streamgage.longitude, streamgage.lat_long_type, streamgage.country, streamgage.hydrologic_unit, streamgage.drainage_area, streamgage.datum_of_page, streamgage.datum_type] for streamgage in alaska_streamgages_data]

    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="alaska_streamgages_data.csv"'

    # Write CSV content
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

    return response

def download_simpson_lagoon_csv(request):
    # Query data from MySQL
    simpson_lagoon_data = simpsonLagoon.objects.all()

    # Define CSV header and rows
    csv_header = ['Sample ID', 'Type', 'Volume', 'Mid Sampling', 'Season', 'Year', 'Latitude', 'Longitude', 'Salinity', 'Temperature', 'Radium224', 'Error224', 'Radium223', 'Error223', 'Radium228', 'Error228', 'Radium226', 'Error226']
    csv_rows = [[lagoon.sample_ID, lagoon.type, lagoon.volume, lagoon.mid_sampling, lagoon.season, lagoon.year, lagoon.latitude, lagoon.longitude, lagoon.salinity, lagoon.temperature, lagoon.radium224, lagoon.error224, lagoon.radium223, lagoon.error223, lagoon.radium228, lagoon.error228, lagoon.radium226, lagoon.error226] for lagoon in simpson_lagoon_data]

    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="simpson_lagoon_data.csv"'

    # Write CSV content
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

    return response