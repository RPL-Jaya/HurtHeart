from django.db import models
from authentication.models import User
from psikiater.models import Psikiater

# Create your models here.

class PasienManager(models.Manager):
    # List of Pasien
    def list_pasien(self):
        return self.all()

    # Create Pasien
    def create_pasien(self, data):
        Pasien = self.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            role='patient'
        )
        return Pasien
    
class Pasien(User):
    objects = PasienManager()

class Ulasan(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    psikiater = models.ForeignKey(Psikiater, on_delete=models.CASCADE)
    komentar = models.TextField()
    rating = models.FloatField()
    tanggalKonsultasi = models.DateField()
    namaPsikiater = models.CharField(max_length=100)

class PesananKonsultasi(models.Model):
    pasien = models.CharField(max_length=255)
    jadwal_konsultasi = models.ForeignKey('psikiater.JadwalKonsultasi', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pasien} - {self.jadwal_konsultasi}"

class Pembayaran(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    metodePembayaran = models.TextField()
    buktiPembayaran = models.TextField()
    statusPembayaran = models.TextField()
    # timestamp = models.DateTimeField()

