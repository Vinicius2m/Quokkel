from rest_framework.urls import path
from users.views import AdminView

urlpatterns = [
    path("admin/", AdminView.as_view()),
    path("admin/register/", AdminView.as_view()),
    path("admin/<str:admin_id>", AdminView.as_view()),
]
