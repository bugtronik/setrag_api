from django.db import models

class Seat(models.Model):
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=200)
    date_depart =  models.CharField(max_length=20)
    heure_depart =  models.CharField(max_length=20)
    departure_station = models.CharField(max_length=20)
    arrival_station = models.CharField(max_length=20)
    seat_occupation_flag = models.SmallIntegerField(null=True)
    
    def __str__(self)-> str:
        return self.number
