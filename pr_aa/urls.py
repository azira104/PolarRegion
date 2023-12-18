from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_aa'

urlpatterns = [
    path('seaice', views.seaice, name='seaice'),
    path('sulfurDioxide', views.sulfurDioxide, name='sulfurDioxide'),
    path('aa1', views.aa1, name='aa1')
]