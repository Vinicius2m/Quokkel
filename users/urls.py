from rest_framework.urls import path
from users.views import AdminView

urlpatterns = [
    path("admin/register/", AdminView.as_view()),
]
