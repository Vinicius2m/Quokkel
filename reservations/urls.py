from django.urls import path

from reservations.views import (
    ReservationsView,
    RetrieveReservationsView,
    UpdateReservationsView,
)

urlpatterns = [
    path("reservations/", ReservationsView.as_view()),
    path("reservations/guest/<str:guest_id>/", ReservationsView.as_view()),
    path("reservations/register/<str:room_category_id>/", ReservationsView.as_view()),
    path(
        "reservations/retrieve/<str:reservation_id>/",
        RetrieveReservationsView.as_view(),
    ),
    path("reservations/<str:reservation_id>/", UpdateReservationsView.as_view()),
]
