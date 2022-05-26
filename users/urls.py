from rest_framework.urls import path
from users.views import AdminView

urlpatterns = [
    path("register/", AdminView.as_view()),
]
