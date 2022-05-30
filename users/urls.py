from rest_framework.urls import path

from users.views import AdminView, GuestsView, UsersView

urlpatterns = [
    path("admins/register/", AdminView.as_view()),              # post register adm
    path("admins/login/", UsersView.as_view()),                 # post login adm
    path("admins/<str:admin_id>/", AdminView.as_view()),        # patch, delete adm
    path("guests/register/", GuestsView.as_view()),             # post register guest
    path("guests/login/", UsersView.as_view()),                 # post login guest
    path("guests/<str:guest_id>/", GuestsView.as_view()),       # patch, delete guest
    path("users/", UsersView.as_view()),                        # get all users
    path("users/admins/", UsersView.as_view()),                 # get all admins
    path("users/admins/<str:user_id>/", UsersView.as_view()),   # get admin by id
    path("users/guests/", UsersView.as_view()),                 # get all guests
    path("users/guests/<str:user_id>/", UsersView.as_view()),   # get guest by id
]
