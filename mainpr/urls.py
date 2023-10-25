from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'mainpr'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('topics-detail/', views.tDetail, name='topics-detail'),
    path('topics-listing/', views.tListing, name='topics-listing'),
]