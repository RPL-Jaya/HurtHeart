# Generated by Django 4.2.7 on 2023-12-12 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasien', '0007_ulasan_pesanan_alter_pesanankonsultasi_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ulasan',
            name='namaPsikiater',
        ),
        migrations.RemoveField(
            model_name='ulasan',
            name='tanggalKonsultasi',
        ),
    ]