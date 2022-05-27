from django.urls import path

from reservations.views import ReservationsView

urlpatterns = [path("reservations/<str:room_category_id>/", ReservationsView.as_view())]
