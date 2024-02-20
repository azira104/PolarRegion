from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# calling from models.py
from .models import nucleotideRead, edaphicFactors, C14_C13_data

# Create your views here.
def bacteria(request):
    return render(request, 'bacteria.html')

def iceKrill(request):
    return render(request, 'iceKrill.html')

def phytoplankton(request):
    return render(request, 'phytoplankton.html')

def plankton(request):
    return render(request, 'plankton.html')

def Cdata(request):
    Cdata_data = C14_C13_data.objects.all()
    return render(request, 'Cdata.html', {'Cdata': Cdata_data})

def edaphic(request):
    edaphic_data = edaphicFactors.objects.all()
    return render(request, 'edaphic.html', {'edaphic': edaphic_data})

def nucleotide(request):
    nucleotide_data = nucleotideRead.objects.all()
    return render(request, 'nucleotide.html', {'nucleotide': nucleotide_data})
