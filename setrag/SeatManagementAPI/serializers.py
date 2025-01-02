from rest_framework import serializers

class SeatAvailableSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    number = serializers.CharField(max_length=20)
    label = serializers.CharField(max_length=200)
    date_depart = serializers.CharField(max_length=20)
    heure_depart = serializers.CharField(max_length=20)
    departure_station = serializers.CharField(max_length=20)
    arrival_station = serializers.CharField(max_length=20)
    seat_occupation_flag = serializers.IntegerField()