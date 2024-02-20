from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_plant'

urlpatterns = [
    path('microbial', views.microbial, name='microbial'),
    path('algae', views.algae, name='algae'),
     path('download-microbial-symbionts-csv/', views.download_microbial_symbionts_csv, name='download_microbial_symbionts_csv'),
     path('download-glacier-algae-csv/', views.download_glacier_algae_csv, name='download_glacier_algae_csv'),
]