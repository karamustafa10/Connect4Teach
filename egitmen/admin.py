from django.contrib import admin
from .models import Cevaplar, Sorular, CalismaKagitlari

class CevaplarAdmin(admin.ModelAdmin):
    list_display = ("yazar", "cevap_metni")
    search_fields = ("yazar", "cevap_metni")  

class SorularAdmin(admin.ModelAdmin):
    list_display = ("ders", "konu", "sinif", "yazar", "cevaplandi_mi")
    search_fields = ("ders", "konu", "sinif", "yazar")

class CalismaKagitlariAdmin(admin.ModelAdmin):
    list_display = ("ders", "konu", "sinif", "yazar")
    search_fields = ("ders", "konu", "sinif", "yazar")

admin.site.register(Sorular, SorularAdmin)
admin.site.register(Cevaplar, CevaplarAdmin)
admin.site.register(CalismaKagitlari, CalismaKagitlariAdmin)