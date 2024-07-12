from django.urls import path
from . import views

# http://127.0.0.1:8000/                 => index
# http://127.0.0.1:8000/egitmen_anasayfa => eğitmen anasayfası

urlpatterns = [
    path("egitmen-anasayfa", views.egitmen_anasayfa, name="egitmen_anasayfa"),
    path("ogrenciler", views.ogrenciler, name="ogrenciler"),
    path("cevaplanmis-sorular", views.cevaplanmis_sorular, name="cevaplanmis_sorular"),
    path("cevaplanmamis-sorular", views.cevaplanmamis_sorular, name="cevaplanmamis_sorular"),
    path("calisma-kagitlari", views.calisma_kagitlari, name="calisma_kagitlari"),
    path('profil/<int:id>', views.profil, name='profil'),
    path('profilim', views.profilim, name='profilim'),
    path('cevap-gonder/', views.cevap_gonder, name='cevap_gonder'),
    path('add_calismak/', views.add_calismak, name='add_calismak'),
]