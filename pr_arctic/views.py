from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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