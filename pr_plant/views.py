from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv

# calling from models.py
from .models import microbialSymbionts, glacierAlgae

# Create your views here.
def microbial(request):
    microbial_data = microbialSymbionts.objects.all()
    return render(request, 'microbial.html', {'microbial': microbial_data})

def algae(request):
    algae_data = glacierAlgae.objects.all()
    return render(request, 'algae.html', {'algae': algae_data})

def download_glacier_algae_csv(request):
    glacier_algae_data = glacierAlgae.objects.all()
    csv_header = ['ID', 'Type', 'F', 'Fm', 'Par', 'Y', 'Etr', 'Rep', 'Treat', 'Npq', 'Etrmax', 'Alpha', 'Ek']
    csv_rows = [[ga.id, ga.type, ga.f, ga.fm, ga.par, ga.y, ga.etr, ga.rep, ga.treat, ga.npq, ga.etrmax, ga.alpha, ga.ek] for ga in glacier_algae_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="glacier_algae_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response

def download_microbial_symbionts_csv(request):
    microbial_symbionts_data = microbialSymbionts.objects.all()
    csv_header = ['ID', 'Plant', 'Response', 'Response Unit', 'Mean', 'N', 'Dispersion Value', 'Dispersion Measure', 'Cold Condition', 'Temperature', 'Infection Status', 'Microorganism', 'Comment']
    csv_rows = [[ms.id, ms.plant, ms.response, ms.response_unit, ms.mean, ms.n, ms.dispersion_value, ms.dispersion_measure, ms.cold_condition, ms.temperature, ms.infection_status, ms.microorganism, ms.comment] for ms in microbial_symbionts_data]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="microbial_symbionts_data.csv"'
    writer = csv.writer(response)
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
    return response