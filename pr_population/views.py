from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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