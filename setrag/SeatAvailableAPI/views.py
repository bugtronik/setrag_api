from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SeatAvailable
from .serializers import SeatAvailableSerializer

@api_view()
def trains(request):
    
    seats_available = SeatAvailable.objects.raw("""
                            SELECT t.id,
                                    t.number,
                            	   tp.label,
                                   DATE_FORMAT(FROM_UNIXTIME(t.planned_date/1000), "%%d/%%m/%%Y"),
                                   DATE_FORMAT(FROM_UNIXTIME(t.planned_date/1000), "%%H:%%i"),
                                   IF(wdr.departure_station = 1, "OWENDO VIRIE", "FRANCEVILLE"),
                                   IF(wdr.arrival_station = 23, "FRANCEVILLE", "OWENDO VIRIE"),
                            	   count(sbr.seat_occupation_flag)
                            FROM train AS t
                            INNER JOIN seat_booking_record AS sbr
                            ON sbr.train_id = t.id
                            INNER JOIN seat AS s
                            ON s.id = sbr.seat_id
                            INNER JOIN car AS c
                            ON c.id = s.car_id
                            INNER JOIN train_type tp
                            ON t.train_type_id = tp.id
                            INNER JOIN week_day_route  wdr
                            ON wdr.id = t.week_day_route_id
                            WHERE
                            (t.planned_date/1000) BETWEEN UNIX_TIMESTAMP('2024-01-01 00:00:00') AND UNIX_TIMESTAMP('2024-01-31 23:59:59')
                            AND sbr.seat_occupation_flag = 0 AND tp.label IN ('EXPRESS', 'OMNIBUS')
                            GROUP BY DATE_FORMAT(FROM_UNIXTIME(t.planned_date/1000), "%%d/%%m/%%Y"), t.number
                        """)
    serialized_seat_available = SeatAvailableSerializer(seats_available, many=True)
    return Response(serialized_seat_available.data)