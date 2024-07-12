from django.urls import path
from . import views

urlpatterns = [
    path("giris-yap", views.giris_yap, name="giris_yap"),
    path("kayit-ol", views.kayit_ol, name="kayit_ol"),
    path("cikis-yap", views.cikis_yap, name="cikis_yap"),
]
