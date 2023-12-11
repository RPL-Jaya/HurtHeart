# Generated by Django 4.2.7 on 2023-12-03 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('psikiater', '0002_jadwal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jadwal',
            old_name='jam',
            new_name='jam_mulai',
        ),
        migrations.RenameField(
            model_name='jadwal',
            old_name='kuota_terserdia',
            new_name='kuota_tersedia',
        ),
        migrations.AddField(
            model_name='jadwal',
            name='jam_selesai',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
