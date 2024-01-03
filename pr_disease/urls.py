from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_disease'

urlpatterns = [
    path('bELISA', views.bELISA, name='bELISA'),
    path('hi', views.hi, name='hi'),
    path('crypto_giardia', views.crypto_giardia, name='crypto_giardia')
]