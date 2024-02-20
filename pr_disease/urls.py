from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_disease'

urlpatterns = [
    path('bELISA', views.bELISA, name='bELISA'),
    path('hi', views.hi, name='hi'),
    path('crypto_giardia', views.crypto_giardia, name='crypto_giardia'),
    path('download-birdinfluenza-belisa-csv/', views.download_birdinfluenza_belisa_csv, name='download_birdinfluenza_belisa_csv'),
path('download-birdinfluenza-hi-csv/', views.download_birdinfluenza_hi_csv, name='download_birdinfluenza_hi_csv'),
    path('download-wildlife-cysts-oocysts-csv/', views.download_wildlife_cysts_oocysts_csv, name='download_wildlife_cysts_oocysts_csv'),
]