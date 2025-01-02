from django.db import models

class SeatAvailable(models.Model):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=200)
    date_depart = models.IntegerField()
    #heure_depart = models.IntegerField()
    departure_station = models.SmallIntegerField(null=True)
    arrival_station = models.SmallIntegerField(null=True)
    seat_occupation_flag = models.SmallIntegerField(null=True)
    
class Seat(models.Model):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=200)
    date_depart = models.IntegerField()
    heure_depart = models.IntegerField()
    departure_station = models.SmallIntegerField(null=True)
    arrival_station = models.SmallIntegerField(null=True)
    seat_occupation_flag = models.SmallIntegerField(null=True)