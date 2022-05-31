from django.urls import path

from .views import RoomDetailView, RoomStatusView, RoomView

urlpatterns = [
    path("rooms/", RoomView.as_view()),
    path("rooms/room/<str:room_id>/", RoomDetailView.as_view()),
    path("rooms/room_category/<str:room_category_id>/", RoomView.as_view()),
    path("rooms/<str:room_category_id>/", RoomStatusView.as_view()),
]
