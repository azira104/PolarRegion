from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_antartic'

urlpatterns = [
    path('AntarcticaRoutes/', views.AntarcticaRoutes, name='AntarcticaRoutes'),
    path('antartic1/', views.antartic1, name='antartic1'),
    path('antartic2/', views.antartic2, name='antartic2'),
    path('antarticmass', views.antarticmass, name='antarticmass'),
    path('hotpoints', views.hotpoints, name='hotpoints'),
    path('iceradar/',views.iceradar, name='iceradar'),
    path('snow/',views.snow, name='snow'),
#    path('download_antarctic_mass_csv/', views.download_antarctic_mass_csv, name='download_antarctic_mass_csv'),
#     path('download_antarctic_hotpoints_csv/', views.download_antarctic_hotpoints_csv, name='download_antarctic_hotpoints_csv'),
]