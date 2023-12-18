from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_population'

urlpatterns = [
    path('penguinpopu/', views.penguinpopu, name='penguinpopu'),
    path('palmer/', views.palmer, name='palmer'),
    path('mfungi/', views.mfungi, name='mfungi'),
]