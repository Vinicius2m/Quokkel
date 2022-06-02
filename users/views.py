from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsGuest, IsStaff, UsersViewPermission
from users.serializers import AdminSerializer, GuestsSerializer, LoginSerializer


class AdminView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def post(self, request):

        serializer = AdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_user = User.objects.filter(
            email=serializer.validated_data["email"]
        ).exists()

        if found_user:
            return Response({"error": "Admin already exists"}, status.HTTP_409_CONFLICT)

        serializer.validated_data["password"] = make_password(
            serializer.validated_data["password"]
        )

        try:
            user = User.objects.create(**serializer.validated_data)
        except IntegrityError as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)

        serializer = AdminSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, request, admin_id):

        if not request.data:
            return Response({"error": "Data is required"}, status=status.HTTP_400_BAD_REQUEST)

        if len(admin_id) != 36:
            return Response(
                {"error": "admin_id must be a valid uuid"}, status=status.HTTP_404_NOT_FOUND
            )

        user = User.objects.filter(user_id=admin_id)

        serializer = AdminSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get("password"):
            serializer.validated_data["password"] = make_password(
                serializer.validated_data["password"]
            )

        try:
            user.update(**serializer.validated_data)
        except IntegrityError as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)

        user: User = user.first()

        serializer = AdminSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, _, admin_id):
        if len(admin_id) != 36:
            return Response(
                {"error": "admin_id must be a valid uuid"}, status=status.HTTP_404_NOT_FOUND
            )

        user = User.objects.filter(user_id=admin_id)

        if not user.exists():
            return Response({"error": "Admin not found"}, status.HTTP_404_NOT_FOUND)

        try:
            user.delete()
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)

        return Response("", status.HTTP_204_NO_CONTENT)


class GuestsView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsGuest]

    def post(self, request):

        serializer = GuestsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            found_guest = User.objects.filter(
                email=serializer.validated_data["email"]
            ).exists()

            if found_guest:
                return Response(
                    {"error": "Guest already exists"}, status.HTTP_409_CONFLICT
                )

            guest: User = User.objects.create(**serializer.validated_data)
            guest.set_password(serializer.validated_data["password"])
            guest.save()

            serializer = GuestsSerializer(guest)

            return Response(serializer.data, status.HTTP_201_CREATED)

        except IntegrityError as error:
            return Response({"error": str(error)}, status.HTTP_409_CONFLICT)

    def patch(self, request, guest_id):

        if not request.data:
            return Response({"error": "Data is required"}, status=status.HTTP_400_BAD_REQUEST)

        if len(guest_id) != 36:
            return Response(
                {"error": "guest_id must be a valid uuid"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = GuestsSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            guest: User = User.objects.filter(user_id=guest_id)
            guest.update(**serializer.validated_data)

            guest: User = guest.first()

            if serializer.validated_data.get("password"):
                guest.set_password(serializer.validated_data.get("password"))
                guest.save()

            serializer = GuestsSerializer(guest)

            return Response(serializer.data, status.HTTP_200_OK)

        except IntegrityError as error:
            if "unique" in str(error).lower():
                return Response(
                    {"error": "Email already exists."}, status.HTTP_409_CONFLICT
                )

    def delete(self, _, guest_id):
        if len(guest_id) != 36:
            return Response(
                {"error": "guest_id must be a valid uuid"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            guest: User = User.objects.filter(user_id=guest_id)
            guest.delete()

            return Response("", status.HTTP_204_NO_CONTENT)

        except ValidationError as error:
            return Response({"error": error}, status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [UsersViewPermission]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        path = self.request.get_full_path()

        if "admin" in path:
            user = User.objects.filter(
                email=serializer.validated_data["email"], is_staff=True
            ).first()

            if not user:
                return Response({"error": "Admin not found"}, status.HTTP_404_NOT_FOUND)

        if "guest" in path:
            user = User.objects.filter(
                email=serializer.validated_data["email"], is_staff=False
            ).first()

            if not user:
                return Response({"error": "Guest not found"}, status.HTTP_404_NOT_FOUND)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response(
                {"error": "Invalid credentials."}, status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status.HTTP_200_OK)

    def get(self, _, user_id=None):
        

        path = self.request.get_full_path()

        if user_id:
            if len(user_id) != 36:
                return Response(
                    {"error": "user_id must be a valid uuid"}, status=status.HTTP_404_NOT_FOUND
                )
            user = User.objects.filter(user_id=user_id).first()

            if user.is_staff and "/admins" not in path:
                return Response({"error": "Guest not found"}, status.HTTP_404_NOT_FOUND)

            if not user.is_staff and "/guests" not in path:
                return Response({"error": "Admin not found"}, status.HTTP_404_NOT_FOUND)

            if not user:
                return Response({"error": "User not found"}, status.HTTP_404_NOT_FOUND)

            serializer = AdminSerializer(user)

            return Response(serializer.data, status.HTTP_200_OK)

        if "guests" not in path and "admins" not in path:
            users = users = User.objects.all()
            serializer = AdminSerializer(users, many=True)

            return Response(serializer.data, status.HTTP_200_OK)

        users = User.objects.filter(is_staff=False).all()

        if "admins" in path:
            users = User.objects.filter(is_staff=True).all()

        serializer = AdminSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
