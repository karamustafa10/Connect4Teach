from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from egitmen.models import Cevaplar, CalismaKagitlari, Sorular
from django.contrib.auth.decorators import login_required
from hesap.models import Uyeler
from django.views.decorators.csrf import csrf_exempt
import json

lesson_areas = ["Matematik", "Fizik", "Kimya", "Edebiyat", "Tarih", "Biyoloji"]
student_classes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

@login_required
def egitmen_anasayfa(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    context = {
        "ogrenciler": Uyeler.objects.filter(membership_type = "student"),
        'uye': current_user,
    }

    return render(request, "egitmen/egitmen-anasayfa.html", context)


@login_required
def ogrenciler(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    context = {
        "ogrenciler": Uyeler.objects.filter(membership_type = "student"),
        'uye': current_user,
    }
    return render(request, "egitmen/ogrenciler.html", context)

@login_required
def cevaplanmis_sorular(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)
    ders_filtre = request.GET.get('ders_filtre')

    if ders_filtre in lesson_areas:
        sorular = Sorular.objects.filter(cevaplandi_mi = True, ders=ders_filtre)
    else:
        sorular = Sorular.objects.filter(cevaplandi_mi = True)

    context = {
        "sorular": sorular,
        'uye': current_user,
        'lesson_areas': lesson_areas
    }
    return render(request, "egitmen/cevaplanmis-sorular.html", context)

@login_required
def cevaplanmamis_sorular(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)
    ders_filtre = request.GET.get('ders_filtre')

    if ders_filtre in lesson_areas:
        sorular = Sorular.objects.filter(cevaplandi_mi = False, ders=ders_filtre)
    else:
        sorular = Sorular.objects.filter(cevaplandi_mi = False)

    context = {
        "sorular": sorular,
        'uye': current_user,
        'lesson_areas': lesson_areas
    }
    return render(request, "egitmen/cevaplanmamis-sorular.html", context)

@login_required
def calisma_kagitlari(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    context = {
        "calisma_kagitlari": CalismaKagitlari.objects.all(),
        'uye': current_user,
    }
    return render(request, "egitmen/calisma-kagitlari.html", context)

@login_required
def profil(request, id):

    profil = Uyeler.objects.get(pk=id)

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    ders_filtre = request.GET.get('ders_filtre')
    if ders_filtre in lesson_areas:
        sorular = Sorular.objects.filter(idogrenci=profil.id, ders=ders_filtre)
    else:
        sorular = Sorular.objects.filter(idogrenci=profil.id)

    context = {
        "profil": profil,
        'uye': current_user,
        'sorular': sorular,
        'lesson_areas': lesson_areas
    }

    return render(request, 'egitmen/profil.html', context)


@login_required
def profilim(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)
    
    ders_filtre = request.GET.get('ders_filtre')
    if ders_filtre in lesson_areas:
        calismaK = CalismaKagitlari.objects.filter(idegitmen=current_user.id, ders=ders_filtre)
    else:
        calismaK = CalismaKagitlari.objects.filter(idegitmen=current_user.id)

    context = {
        'uye': current_user,
        'calismaK': calismaK,
        'lesson_areas': lesson_areas
    }
 
    return render(request, 'egitmen/profilim.html', context)

@login_required
def cevap_gonder(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    if request.method == 'POST':
        # Formdan gelen verileri al
        soru_id = request.POST.get('soru_id')
        cevap_metni = request.POST.get('cevap_metni')
        
        # Veritabanına cevabı kaydet
        cevap = Cevaplar.objects.create(soru_id=soru_id, cevap_metni=cevap_metni, yazar=current_user.firstname + " " + current_user.lastname)
        cevap.save()

        soru = get_object_or_404(Sorular, id=soru_id)
        soru.cevaplandi_mi = True
        soru.save()
        
        return redirect("cevaplanmamis_sorular")


@login_required
def add_calismak(request):
       
    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)
    context = {
        'uye': current_user,
    } 
    
    if request.method == "POST":
        dosya = request.FILES.get("dosya")
        ders = request.POST.get("ders")
        konu = request.POST.get("konu")
        sinif = request.POST.get("sinif")
        aciklama = request.POST.get("aciklama")

        if not ders:
            return HttpResponse("Ders alanı seçimi gerekli.", status=400)
        if ders not in lesson_areas:
            return HttpResponse("Geçersiz ders alanı seçimi.", status=400)

        if not sinif:
            return HttpResponse("Sınıf seçimi gerekli.", status=400)
        if sinif not in student_classes:
            return HttpResponse("Geçersiz sınıf seçimi.", status=400)
        
        new_question = CalismaKagitlari(
            idegitmen=current_user.id,
            ders=ders,
            sinif=sinif,
            dosya=dosya,
            konu=konu,
            yazar= current_user.firstname + " " + current_user.lastname,
            aciklama = aciklama
        )
        new_question.save()
        return redirect("add_calismak")
    
    return render(request, 'egitmen/add_calismak.html', context)