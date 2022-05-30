from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsStaff(BasePermission):
    def has_permission(self, request: Request, _):

        restricted_methods = ["GET", "POST", "PATCH", "DELETE", "PUT"]

        if request.method in restricted_methods and (
            request.user.is_anonymous or not request.user.is_staff
        ):
            return False

        return True
