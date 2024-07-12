from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Uyeler
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import default_storage
import os
from django.conf import settings


def giris_yap(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        # Kullanıcıyı authenticate etmek için username olarak email'i kullanıyoruz
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            uye = Uyeler.objects.get(email=email)
            if uye.membership_type == "teacher":
                return redirect("egitmen_anasayfa")
            elif uye.membership_type == "student":
                return redirect("ogrenci_anasayfa")
            else:
                return redirect("ana_sayfa")  # Üyelik türü belirli değilse genel ana sayfa
        else:
            # Hata mesajını dictionary içinde döndür
            return render(request, "hesap/giris-yap.html", {
                "error": "Geçersiz email veya parola.",
                "email": email,
            })
    else:
        return render(request, "hesap/giris-yap.html")



def kayit_ol(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        membership_type = request.POST.get("membership_type")
        field_info = request.POST.get("field_info")  
        photo = request.FILES.get("photo")

        username = email  # Email'i username olarak kullanıyoruz

        if password == repassword:
            if Uyeler.objects.filter(email=email).exists():
                return render(request, "hesap/kayit-ol.html", {
                    "error": "Bu email adresi kullanılmaktadır.",
                    "firstname": firstname,
                    "lastname": lastname,
                    "email": email,
                    "phone": phone,
                    "membership_type": membership_type,
                })
            else:
                if Uyeler.objects.filter(phone=phone).exists():
                    return render(request, "hesap/kayit-ol.html", {
                        "error": "Bu telefon numarası kullanılmaktadır.",
                        "firstname": firstname,
                        "lastname": lastname,
                        "email": email,
                        "phone": phone,
                        "membership_type": membership_type,
                    })
                else:
                    # User modeline kullanıcı oluşturuyoruz
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.first_name = firstname
                    user.last_name = lastname
                    user.save()

                    
                    # Uyeler modeline kullanıcı bilgilerini kaydediyoruz
                    hashed_password = make_password(password)
                    uye = Uyeler.objects.create(
                        firstname=firstname,
                        lastname=lastname,
                        email=email,
                        phone=phone,
                        password=hashed_password,  # Şifreyi hashleyerek kaydediyoruz
                        membership_type=membership_type,
                        field_info=field_info,
                        photo=photo,  # Fotoğrafı kaydediyoruz,
                    )
                    uye.save()
                    return redirect("giris_yap")
        else:
            return render(request, "hesap/kayit-ol.html", {
                "error": "Parolalar eşleşmiyor.",
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "phone": phone,
                "membership_type": membership_type,
            })
    return render(request, "hesap/kayit-ol.html")


def cikis_yap(request):
    logout(request)
    return redirect("anasayfa")