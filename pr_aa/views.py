from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def seaice(request):
    return render(request, 'seaice.html')

def aa1(request):
    return render(request, 'aa1.html')



