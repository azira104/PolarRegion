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
   path('ani-coral/download-csv/', views.download_coral_csv, name='download_coral_csv'),
    path('ani-adelie/download-csv/', views.download_adelie_penguin_csv, name='download_adelie_csv'),
    path('ani-gentoo/download-csv/', views.download_gentoo_penguin_csv, name='download_gentoo_csv'),
    path('ani-chinstrap/download-csv/', views.download_chinstrap_penguin_csv, name='download_chinstrap_csv'),
    path('ani-bird/download-csv/', views.download_giant_petrel_bird_csv, name='download_bird_csv'),
    path('ani-krillbase/download-csv/', views.download_krillbase_csv, name='download_krillbase_csv'),
    path('ani-bear-blood/download-csv/', views.download_bear_blood_csv, name='download_bear_blood_csv'),
    path('ani-bear-abdominal-temp/download-csv/', views.download_bear_abdominal_temp_csv, name='download_bear_abdominal_temp_csv'),
    path('ani-bear-cap-sequence/download-csv/', views.download_bear_cap_sequence_csv, name='download_bear_cap_sequence_csv'),
]
