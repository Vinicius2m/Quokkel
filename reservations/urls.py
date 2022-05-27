from django.urls import path

from reservations.views import ReservationsView, UpdateReservationsView

urlpatterns = [
    path("reservations/register/<str:room_category_id>/", ReservationsView.as_view()),
    path("reservations/<str:reservation_id>/", UpdateReservationsView.as_view()),
]
