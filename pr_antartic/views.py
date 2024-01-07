from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# calling from models.py
from .models import antarcticMass, antarcticHotpoints

# Create your views here.
def antartic(request):
    return render(request, 'antartic.html')

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
