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
    path('streamgages', views.streamgages, name='streamgages')
]