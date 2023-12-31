from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_animal'

urlpatterns = [
    path('coral', views.coral, name='coral'),
    path('krillBase', views.krillBase, name='krillBase'),
    path('gentooPenguin', views.gentooPenguin, name='signyGentooPenguin')
]
