from django.urls import path
from . import views

urlpatterns = [
    path('', views.getroutes, name='api'),
    path('sulfur', views.get_sulfur),
    path('antarctic_mass', views.get_antarctic_mass),
    path('nucleotide_read', views.get_nucleotide_read),
    path('edaphic_factors', views.get_edaphic_factors),
    path('c14_c13_data', views.get_c14_c13_data),
    path('glacier_algae', views.get_glacier_algae),
    path('microbial_symbionts', views.get_microbial_symbionts),
    path('coral', views.get_coral),
    path('giant_petrel_bird', views.get_giant_petrel_bird),
    path('bird_influenza_belisa', views.get_bird_influenza_belisa),
    path('bird_influenza_hi', views.get_bird_influenza_hi),
    path('wildlife_cysts_oocysts', views.get_wildlife_cysts_oocysts),
]



