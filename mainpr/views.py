from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# from .forms import ContactForm
from django.urls import reverse
# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib.staticfiles import finders
from functools import lru_cache
#import response

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from.models import *
@api_view(['GET'])
def getroutes(request):
    routes = [
        'GET /api',]
    
    return Response(routes)
@lru_cache()
def get_logo_data():
    with open(finders.find('images/logo/pbxaibig.png'), 'rb') as f:
        logo_data = f.read()
    return MIMEImage(logo_data)
def send_feedback(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_type = request.POST.get('userType')
        easy_navigation = request.POST.get('easyNavigation')
        issues = request.POST.get('issues', '')
        additional_features = request.POST.get('additionalFeatures', '')
        other_feedback = request.POST.get('otherFeedback', '')

        # Prepare the context for the email
        context = {
            'name': name,
            'user_type': user_type,
            'easy_navigation': easy_navigation,
            'issues': issues,
            'additional_features': additional_features,
            'other_feedback': other_feedback,
        }
        subject = 'New Feedback Received'
        from_email = email
        to = settings.EMAIL_HOST_USER

        html_content = render_to_string('feedback_email.html', context)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        logo = get_logo_data()
        logo.add_header('Content-ID', '<logo>')
        msg.attach(logo)
        try:
            msg.send()
        except Exception as e:
            print(f"Error sending email: {e}")
            return {'message': 'An error occurred while sending the email.', 'bg': 'bg-danger'}



        # Return success response
        return JsonResponse({'status': 'success', 'message': 'Thank you for your feedback!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

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
def haznirah(request):
    return render(request, 'haznirah.html')
def azira(request):
    return render(request, 'azira.html')
def ainin(request):
    return render(request, 'ainin.html')

def ml(request):
    selected_option = request.GET.get('option', None)
    title = "Machine Learning - Polar Region"
    if selected_option == 'microbial_symbionts':
        title = "Classification Plant Tolerance to Chiling and Freezing Condition using Support Vector Machine (SVM)"
    elif selected_option == 'northern_cities_climate':
        title = "Analysis of Temperature Change in Artic Cities"
    elif selected_option == 'crypto_giardia':
        title = "Analyzing Cryptosporidium and Giardia in Arctic Wildlife: Data Visualization"
    elif selected_option == 'fungi':
        title = "Predicting Fungal Abundance in Soil Samples Based on Edaphic Factors Using Random Forest"
    
    context = {
        'selected_option': selected_option,
        'title': title,
    }
    return render(request, 'ml.html', context)

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

# def my_view(request):
#     contact_us_url = reverse('contact_us')
#     return render(request, 'index.html', {'contact_us_url': contact_us_url})

