from django.urls import path

from reservations.views import ReservationsView

urlpatterns = [
    path("reservations/<str:room_category_id>/", ReservationsView.as_view()),
    path("reservations/guest/<str:guest_id>/", ReservationsView.as_view()),
    path("reservations/", ReservationsView.as_view()),
]
