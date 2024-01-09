from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# calling from models.py
from .models import birdInfluenza_bELISA, birdInfluenza_HI, wildlife_cysts_oocysts

# Create your views here.
def bELISA(request):
    bELISA_data = birdInfluenza_bELISA.objects.all()
    return render(request, 'bELISA.html', {'bELISA': bELISA_data})

def hi(request):
    hi_data = birdInfluenza_HI.objects.all()
    return render(request, 'hi.html', {'hi': hi_data})

def crypto_giardia(request):
    crypto_giardia_data = wildlife_cysts_oocysts.objects.all()
    return render(request, 'crypto_giardia.html', {'crypto_giardia': crypto_giardia_data})