from django.db import models
from authentication.models import User



# Create your models here.

class PsikiaterManager(models.Manager):
    # List of psikiater
    def list_psikiater(self):
        return self.all()

    # Create psikiater
    def create_psikiater(self, data):
        psikiater = self.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            role='psychiatrist',
            kualifikasi=data['kualifikasi'],
            ulasanKonsultasi=data['ulasanKonsultasi'],
            jadwalKonsultasi=data['jadwalKonsultasi'],
        )
        return psikiater
class Psikiater(User):
    objects = PsikiaterManager()
    kualifikasi = models.BooleanField(default=False)
    ulasanKonsultasi = models.TextField(default="")
    jadwalKonsultasi = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['kualifikasi', 'ulasanKonsultasi', 'jadwalKonsultasi']


class JadwalKonsultasi(models.Model):
    psikiater = models.CharField(max_length=255)
    tanggal = models.DateTimeField()
    ketersediaan = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.psikiater} - {self.tanggal}"


