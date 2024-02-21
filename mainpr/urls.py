from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'mainpr'

urlpatterns = [
    path('polar', views.index, name='index'),
    path('machine-learning/', views.ml, name='ml'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('team/Dr.Akmal', views.drakmal, name='drakmal'),
    path('team/Dr.mae',views.drmae, name='drmae'),
    path('team/Dr.Alfonso',views.dralfonso, name='dralfonso'),
    path('team/Dr.Ismail',views.drismail, name='drismail'),
    path('team/Dr.Chin',views.drchin, name='drchin'),
    path('team/Prof.Saberi',views.profsaberi, name='profsaberi'),
    path('team/Dr.Sarahani',views.drsarahani, name='drsarahani'),
    path('team/Haznirah',views.haznirah, name='haznirah'),
    path('team/Azira',views.azira, name='azira'),
]