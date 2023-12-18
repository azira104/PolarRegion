from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_dna_rna'

urlpatterns = [
    path('bacteria/', views.bacteria, name='bacteria'),
    path('iceKrill/', views.iceKrill, name='iceKrill'),
    path('phytoplankton/', views.phytoplankton, name='phytoplankton'),
    path('plankton/', views.plankton, name='plankton'),
]