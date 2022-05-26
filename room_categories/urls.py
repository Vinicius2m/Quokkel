from django.urls import path, re_path

from .views import RoomCategoriesView

urlpatterns = [
    path("rooms_categories/<str:room_category_id>", RoomCategoriesView.as_view()),
    re_path(r"^rooms_categories/$", RoomCategoriesView.as_view()),
]
