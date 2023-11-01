from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'mainpr'

urlpatterns = [
    path('', views.index, name='index'),
    path('inner-page/', views.inner_page, name='inner-page'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
]