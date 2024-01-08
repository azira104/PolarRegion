from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def drakmal(request):
    return render(request, 'drakmal.html')

def drmae(request):
    return render(request, 'drmae.html')
def dralfonso(request):
    return render(request, 'dralfonso.html')
def drismail(request):
    return render(request, 'drismail.html')
def drchin(request):
    return render(request, 'drchin.html')
def profsaberi(request):
    return render(request, 'profsaberi.html')
def drsarahani(request):
    return render(request, 'drsarahani.html')

def inner_page(request):
    return render(request, 'inner-page.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')


