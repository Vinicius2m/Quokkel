from django.urls import path, re_path

from room_categories.views import RoomCategoriesView

urlpatterns = [
    path("rooms_categories/", RoomCategoriesView.as_view()),
    path("rooms_categories/<str:room_category_id>/", RoomCategoriesView.as_view()),
]
