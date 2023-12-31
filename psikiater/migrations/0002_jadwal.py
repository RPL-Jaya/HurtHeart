# Generated by Django 4.2.7 on 2023-12-03 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('psikiater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('jam', models.TimeField()),
                ('metode', models.CharField(max_length=255)),
                ('keterangan', models.CharField(max_length=255)),
                ('kuota_total', models.IntegerField()),
                ('kuota_terserdia', models.IntegerField()),
                ('psikiater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
