from django.shortcuts import render, redirect

# Create your views here.

def anasayfa(request):
    return render(request, "anasayfa/anasayfa.html")
    

def hakkimizda(request):
    return render(request, "anasayfa/hakkimizda.html")

def iletisim(request):
    return render(request, "anasayfa/iletisim.html")