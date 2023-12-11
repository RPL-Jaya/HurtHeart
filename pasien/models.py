from django.db import models
from authentication.models import User
from psikiater.models import Psikiater, Jadwal

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

# class Pesanan(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pesanan_user')
#     psikiater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pesanan_psikiater')
#     tanggal_pesan = models.DateField()
#     waktu_mulai = models.TimeField()
#     waktu_selesai = models.TimeField()

#     def __str__(self):
#         return f'{self.user.username} - {self.psikiater.username} - {self.tanggal_pesan}'

class PesananKonsultasi(models.Model):
    BAYAR = "bayar"
    VERIFY = "verify"
    PENDING = "pending"
    SCHED = "scheduled"
    DONE = "done"
    
    STATUS_KONSULTASI_CHOICES = [
        (BAYAR, "Menunggu Pembayaran"),
        (VERIFY, "Menunggu Verifikasi Admin"),
        (PENDING, "Menunggu Konfirmasi Psikiater"),
        (SCHED, "Konsultasi Terjadwal"),
        (DONE, "Selesai")
    ]

    pasien = models.CharField(max_length=255)
    jadwal_konsultasi = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=9,
        choices=STATUS_KONSULTASI_CHOICES,
        default=BAYAR
    )

    def __str__(self):
        return f"{self.pasien} - {self.jadwal_konsultasi}"

class Pembayaran(models.Model):
    OTS = "ots"
    CARD = "card"
    VA = "va"
    EWALLET = "ewallet"
    RETAIL = "retail"

    METODE_PEMBAYARAN_CHOICE = [
        (OTS, "Bayar di tempat"),
        (CARD, "Kartu Kredit/Kartu Debit"),
        (VA, "Virtual Account"),
        (EWALLET, "E-Wallet"),
        (RETAIL, "Gerai Retail"),
    ]

    pesanan = models.ForeignKey(PesananKonsultasi, on_delete=models.CASCADE)
    biayaPembayaran = models.FloatField()
    metodePembayaran = models.CharField(
        max_length=7,
        choices=METODE_PEMBAYARAN_CHOICE,
    )
    buktiPembayaran = models.ImageField(upload_to='images')
    statusPembayaran = models.BooleanField(default=False)
    # timestamp = models.DateTimeField()

