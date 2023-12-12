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
        )
        return psikiater
    
class Psikiater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    kualifikasi = models.BooleanField(default=False)
    ulasanKonsultasi = models.TextField(default="")

    REQUIRED_FIELDS = ['kualifikasi', 'ulasanKonsultasi']

class Jadwal(models.Model):
    psikiater = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    metode = models.CharField(max_length=255)
    keterangan = models.CharField(max_length=255)
    kuota_total = models.IntegerField()
    kuota_tersedia = models.IntegerField()
