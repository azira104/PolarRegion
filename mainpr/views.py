from collections import Counter
from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
# from .forms import ContactForm
from django.urls import reverse

from .models import VisitorLog


# Create your views here.
def index(request):
    return render(request, 'index.html')


def visitor_analytics(request):
    visitor_records = list(VisitorLog.objects.all())

    unique_visitors = VisitorLog.objects.values('visitor_key').distinct().count()
    total_page_views = VisitorLog.objects.count()

    today = timezone.now().date()
    today_count = VisitorLog.objects.filter(accessed_at__date=today).values('visitor_key').distinct().count()

    week_start = today - timedelta(days=7)
    week_count = VisitorLog.objects.filter(accessed_at__date__gte=week_start).values('visitor_key').distinct().count()

    month_start = today - timedelta(days=30)
    month_count = VisitorLog.objects.filter(accessed_at__date__gte=month_start).values('visitor_key').distinct().count()

    page_counts = Counter(record.page_path for record in visitor_records)
    country_counts = Counter(record.country for record in visitor_records)
    device_counts = Counter(record.device_type for record in visitor_records)
    traffic_counts = Counter(record.traffic_source for record in visitor_records)

    most_visited_pages = page_counts.most_common(5)
    top_countries = country_counts.most_common(5)
    top_devices = device_counts.most_common(3)
    top_sources = traffic_counts.most_common(4)

    context = {
        'total_visitors': unique_visitors,
        'total_page_views': total_page_views,
        'visitors_today': today_count,
        'visitors_this_week': week_count,
        'visitors_this_month': month_count,
        'most_visited_pages': most_visited_pages,
        'top_countries': top_countries,
        'top_devices': top_devices,
        'top_sources': top_sources,
    }
    return render(request, 'visitor_analytics.html', context)

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
def haznirah(request):
    return render(request, 'haznirah.html')
def azira(request):
    return render(request, 'azira.html')

def ml(request):
    return render(request, 'ml.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

# def my_view(request):
#     contact_us_url = reverse('contact_us')
#     return render(request, 'index.html', {'contact_us_url': contact_us_url})

