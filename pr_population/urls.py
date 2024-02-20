from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_population'

urlpatterns = [
    path('penguinpopu', views.penguinpopu, name='penguinpopu'),
    path('palmerIter', views.palmerIter, name='palmerIter'),
    path('palmerSize', views.palmerSize, name='palmerSize'),
    path('mfungi', views.mfungi, name='mfungi'),
    path('download-penguin-population-csv/', views.download_penguin_population_csv, name='download_penguin_population_csv'),

]