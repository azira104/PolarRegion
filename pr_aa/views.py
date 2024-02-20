from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv

# calling from models.py
from .models import sulfur

# Create your views here.
def seaice(request):
    return render(request, 'seaice.html')

def sulfurDioxide(request):
    sulfur_data = sulfur.objects.all()
    return render(request, 'sulfurDioxide.html', {'sulfur': sulfur_data})

def aa1(request):
    return render(request, 'aa1.html')

def download_sulfur_csv(request):
    # Query data from MySQL
    sulfur_data = sulfur.objects.all()

    # Define CSV header and rows
    csv_header = ['Year', 'Neem', 'WDC']
    csv_rows = [[s.year, s.neem, s.wdc] for s in sulfur_data]

    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sulfur_data.csv"'

    # Write CSV content
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

    return response
