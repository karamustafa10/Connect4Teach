from django.db import models


class Sorular(models.Model):
    ders = models.CharField(max_length=50)
    konu = models.CharField(max_length=50)
    sinif = models.CharField(max_length=50)
    yazar = models.CharField(max_length=100)
    idogrenci=models.IntegerField(default=-1)
    aciklama = models.CharField(max_length=100, default='.')
    fotograf = models.ImageField(upload_to="sorular", default='.')
    cevaplandi_mi = models.BooleanField(default=False)


class Cevaplar(models.Model):
    soru = models.ForeignKey(Sorular, on_delete=models.CASCADE, related_name='cevaplar')
    yazar = models.CharField(max_length=100) 
    cevap_metni = models.CharField(max_length=255)

class CalismaKagitlari(models.Model):
    ders = models.CharField(max_length=50)
    konu = models.CharField(max_length=50)
    sinif = models.CharField(max_length=50)
    yazar = models.CharField(max_length=100)
    dosya = models.FileField(upload_to="calisma-kagitlari", default=".")
    idegitmen = models.IntegerField(default=-1)
    aciklama = models.CharField(max_length=100, default='.')
