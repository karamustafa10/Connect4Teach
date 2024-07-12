from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from egitmen.models import Cevaplar, CalismaKagitlari, Sorular
from django.contrib.auth.decorators import login_required
from hesap.models import Uyeler

# Create your views here.
lesson_areas = ["Matematik", "Fizik", "Kimya", "Edebiyat", "Tarih", "Biyoloji"]
student_classes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]


def custom_404(request, exception):
    return render(request, '404.html', status=404)


@login_required
def ogrenci_anasayfa(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    context = {
        "egitmenler": Uyeler.objects.filter(membership_type = "teacher"),
        "uye": current_user
    }

    return render(request, "ogrenci/ogrenci-anasayfa.html", context)



@login_required
def egitmenler(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    context = {
        "egitmenler": Uyeler.objects.filter(membership_type = "teacher"),
        'uye': current_user,
    }
    return render(request, "ogrenci/egitmenler.html", context)


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
        'sorular': sorular,
        'uye': current_user,
        'lesson_areas': lesson_areas
    }
    return render(request, "ogrenci/cevaplanmis-sorular.html", context)

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
        'sorular': sorular,
        'uye': current_user,
        'lesson_areas': lesson_areas
    }
    return render(request, "ogrenci/cevaplanmamis-sorular.html", context)

@login_required
def calisma_kagitlari(request):

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    context = {
        "calisma_kagitlari": CalismaKagitlari.objects.all(),
        'uye': current_user,
    }
    return render(request, "ogrenci/calisma-kagitlari.html", context)

@login_required
def profil(request, id):

    profil = Uyeler.objects.get(pk=id)

    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)

    ders_filtre = request.GET.get('ders_filtre')
    if ders_filtre in lesson_areas:
        calismaK = CalismaKagitlari.objects.filter(idegitmen=profil.id, ders=ders_filtre)
    else:
        calismaK = CalismaKagitlari.objects.filter(idegitmen=profil.id)

    context = {
        "profil": profil,
        'uye': current_user,
        'calismaK': calismaK,
        'lesson_areas': lesson_areas
    }

    return render(request, 'ogrenci/profil.html', context)


@login_required
def profilim(request):
    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)
    
    ders_filtre = request.GET.get('ders_filtre')
    if ders_filtre in lesson_areas:
        sorular = Sorular.objects.filter(idogrenci=current_user.id, ders=ders_filtre)
    else:
        sorular = Sorular.objects.filter(idogrenci=current_user.id)

    context = {
        'uye': current_user,
        'sorular': sorular,
        'lesson_areas': lesson_areas
    }
 
    return render(request, 'ogrenci/profilim.html', context)

@login_required
def soru_yukle(request):
    
    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)
    context = {
        'uye': current_user,
    } 
    return render(request, 'ogrenci/soru_yukle.html',context)

@login_required
def send_question(request):
       
    user_email = request.user.email
    current_user = get_object_or_404(Uyeler, email=user_email)
    context = {
        'uye': current_user,
    } 
    

    if request.method == "POST":
        image = request.FILES.get("questionimage")
        lesson_area = request.POST.get("lesson_area")
        student_class = request.POST.get("student_class")
        describe = request.POST.get("describe")
        konu = request.POST.get("konu")


        if not lesson_area:
            return HttpResponse("Ders alanı seçimi gerekli.", status=400)
        if lesson_area not in lesson_areas:
            return HttpResponse("Geçersiz ders alanı seçimi.", status=400)

        if not student_class:
            return HttpResponse("Sınıf seçimi gerekli.", status=400)
        if student_class not in student_classes:
            return HttpResponse("Geçersiz sınıf seçimi.", status=400)
        
        new_question = Sorular(
            idogrenci=current_user.id,
            ders=lesson_area,
            sinif=student_class,
            aciklama=describe,
            fotograf=image,
            konu=konu,
            yazar= current_user.firstname + " " + current_user.lastname
        )
        new_question.save()
        return redirect("soru_yukle")
    else:
        return HttpResponse("Yalnızca POST isteklerine izin verilir.", status=405)
