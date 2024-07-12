from django.urls import path
from . import views

# http://127.0.0.1:8000/                 => index
# http://127.0.0.1:8000/egitmen_anasayfa => eğitmen anasayfası

urlpatterns = [
    path("ogrenci-anasayfa", views.ogrenci_anasayfa, name="ogrenci_anasayfa"),
    path("egitmenler", views.egitmenler, name="egitmenler"),
    path("cevaplanmis-sorular", views.cevaplanmis_sorular, name="ogrenci_cevaplanmis_sorular"),
    path("cevaplanmamis-sorular", views.cevaplanmamis_sorular, name="ogrenci_cevaplanmamis_sorular"),
    path("calisma-kagitlari", views.calisma_kagitlari, name="ogrenci_calisma_kagitlari"),
    path('profil/<int:id>', views.profil, name='ogrenci_profil'),
    path('profilim', views.profilim, name='ogrenci_profilim'),
    path('soru_yukle', views.soru_yukle, name='soru_yukle'),
    path('send_question', views.send_question, name='send_question'),
]

handler404 = 'ogrenci.views.custom_404'