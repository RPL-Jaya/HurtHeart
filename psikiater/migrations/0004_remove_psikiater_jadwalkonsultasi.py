# Generated by Django 4.2.7 on 2023-12-11 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psikiater', '0003_rename_jam_jadwal_jam_mulai_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psikiater',
            name='jadwalKonsultasi',
        ),
    ]
