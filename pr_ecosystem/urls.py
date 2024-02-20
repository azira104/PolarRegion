from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_ecosystem'

urlpatterns = [
    path('freshwater/', views.freshwater, name='freshwater'),
    path('marine/', views.marine, name='marine'),
    path('terrestrial/', views.terrestrial, name='terrestrial'),
]
