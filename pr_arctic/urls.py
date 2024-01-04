from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_arctic'

urlpatterns = [
    path('climate', views.climate, name='climate'),
    path('iceExtent', views.iceExtent, name='iceExtent'),
    path('climate', views.climate, name='climate'),
    path('climate', views.climate, name='climate'),
]