from rest_framework.urls import path

from users.views import AdminView, GuestsView, UsersView

urlpatterns = [
    path("admin/", AdminView.as_view()),
    path("admin/register/", AdminView.as_view()),
    path("admin/<str:admin_id>", AdminView.as_view()),
    path("admin/login/", UsersView.as_view()),
    path("guests/register/", GuestsView.as_view()),
    path("guests/login/", UsersView.as_view()),
    path("guests/<str:guest_id>", GuestsView.as_view())
]
