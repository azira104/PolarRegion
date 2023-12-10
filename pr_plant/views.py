from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# calling from models.py
from .models import microbialSymbionts, glacierAlgae

# Create your views here.
def microbial(request):
    microbial_data = microbialSymbionts.objects.all()
    return render(request, 'microbial.html', {'microbial': microbial_data})

def algae(request):
    algae_data = glacierAlgae.objects.all()
    return render(request, 'algae.html', {'algae': algae_data})