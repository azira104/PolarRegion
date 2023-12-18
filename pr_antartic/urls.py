from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pr_antartic'

urlpatterns = [
    path('antartic/', views.antartic, name='antartic'),
    path('antartic1/', views.antartic1, name='antartic1'),
    path('antartic2/', views.antartic1, name='antartic2'),
]