from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_arctic'

urlpatterns = [
    path('climate', views.climate, name='climate'),
    path('iceextent', views.iceextent, name='iceextent'),
    path('simpsonlagoon', views.simpsonlagoon, name='simpsonlagoon'),
    path('streamgages', views.streamgages, name='streamgages'),
    path('Icemasking', views.masking, name='masking'),
    path('ArcticSeaRoutes', views.searoutes, name='searoutes'),
   path('download-iceextent-csv/', views.download_ice_extent_csv, name='download_iceextent_csv'),
   path('download-northernclimate-csv/', views.download_northern_climate_csv, name='download_northern_climate_csv'),
    path('download-alaskastreamgages-csv/', views.download_alaska_streamgages_csv, name='download_alaska_streamgages_csv'),
    path('download-simpsonlagoon-csv/', views.download_simpson_lagoon_csv, name='download_simpson_lagoon_csv'),
]