# Generated by Django 5.1.4 on 2025-01-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeatManagementAPI', '0002_alter_seat_arrival_station_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='date_depart',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='seat',
            name='heure_depart',
            field=models.CharField(max_length=20),
        ),
    ]