from django.urls import path, re_path

from .views import RoomDetailView, RoomView

urlpatterns = [
    path("rooms/", RoomView.as_view()),
    path("rooms/room/<str:room_id>/", RoomDetailView.as_view()),
    path("rooms/room_category/<str:room_category_id>/", RoomView.as_view()),
]
