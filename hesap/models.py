from django.db import models

class Uyeler(models.Model):
    # Diğer alanlar
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="uyeler/", default='.')

    # Üyelik türü alanı
    MEMBERSHIP_CHOICES = [
        ('teacher', 'Eğitmen'),
        ('student', 'Öğrenci'),
    ]
    membership_type = models.CharField(max_length=7, choices=MEMBERSHIP_CHOICES)

    field_info = models.CharField(max_length=30, default='.')

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.membership_type})"
