# Generated by Django 5.0.6 on 2024-05-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egitmen', '0004_calismakagitlari_dosya_sorular_fotograf'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorular',
            name='aciklama',
            field=models.CharField(default='.', max_length=100),
        ),
    ]