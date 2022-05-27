from django.urls import path

from reservations.views import ReservationsView


urlpatterns = [path("reservations/", ReservationsView.as_view())]
