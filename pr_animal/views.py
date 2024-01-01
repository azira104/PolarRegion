from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# calling from models.py
from .models import coral, gentooPenguin, adeliePenguin, chinstrapPenguin, giantPetrelBird, krillbase, bearBlood, bearAbdominalTemp, bearCapSequence

# Create your views here.
def ani_coral(request):
    coral_data = coral.objects.all()
    return render(request, 'coral.html', {'coral': coral_data})

def ani_krillbase(request):
    krillbase_data = krillbase.objects.all()
    return render(request, 'krillBase.html', {'krillBase': krillbase_data})

def ani_gentoo(request):
    gentoo_data = gentooPenguin.objects.all()
    return render(request, 'gentoo.html', {'gentoo': gentoo_data})

def ani_adelie(request):
    adelie_data = adeliePenguin.objects.all()
    return render(request, 'adelie.html', {'adelie': adelie_data})

def ani_chinstrap(request):
    chinstrap_data = chinstrapPenguin.objects.all()
    return render(request, 'chinstrap.html', {'chinstrap': chinstrap_data})

def ani_bird(request):
    bird_data = giantPetrelBird.objects.all()
    return render(request, 'bird.html', {'bird': bird_data})

def ani_bearBlood(request):
    bearBlood_data = bearBlood.objects.all()
    return render(request, 'blood.html', {'blood': bearBlood_data})

def ani_bearAbdTemp(request):
    bearAbdTemp_data = bearAbdominalTemp.objects.all()
    return render(request, 'abdTemp.html', {'abdTemp': bearAbdTemp_data})

def ani_bearCapSeq(request):
    bearCapSeq_data = bearCapSequence.objects.all()
    return render(request, 'capSeq.html', {'capSeq': bearCapSeq_data})