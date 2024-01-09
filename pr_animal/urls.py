from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_animal'

urlpatterns = [
    path('coral', views.ani_coral, name='coral'),
    path('krillBase', views.ani_krillbase, name='krillBase'),
    path('gentoo', views.ani_gentoo, name='gentoo'),
    path('adelie', views.ani_adelie, name='adelie'),
    path('chinstrap', views.ani_chinstrap, name='chinstrap'),
    path('bird', views.ani_bird, name='bird'),
    path('blood', views.ani_bearBlood, name='blood'),
    path('abdTemp', views.ani_bearAbdTemp, name='abdTemp'),
    path('capSeq', views.ani_bearCapSeq, name='capSeq'),
]
