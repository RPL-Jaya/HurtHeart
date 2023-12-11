# Generated by Django 4.2.7 on 2023-12-02 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psikiater', '0002_jadwalkonsultasi'),
        ('pasien', '0002_ulasan_chage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PesananKonsultasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasien', models.CharField(max_length=255)),
                ('jadwal_konsultasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psikiater.jadwalkonsultasi')),
            ],
        ),
    ]