from django.urls import path
from SeatManagementAPI import views

urlpatterns = [
    path('seats/', views.seats)
]
