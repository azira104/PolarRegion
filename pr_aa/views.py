from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# calling from models.py
from .models import sulfur

# Create your views here.
def sulfurDioxide(request):
    sulfur_data = sulfur.objects.all()
    return render(request, 'sulfurDioxide.html', {'sulfur': sulfur_data})

def aa1(request):
    return render(request, 'aa1.html')
