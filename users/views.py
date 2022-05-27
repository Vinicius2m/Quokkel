from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsStaff, IsGuest
from users.serializers import (AdminSerializer, GuestsSerializer,
                               LoginSerializer)


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

        user: User = User.objects.create(**serializer.validated_data)
        user.set_password(serializer.validated_data["password"])
        user.save()

        serializer = AdminSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, _, admin_id=None):

        if not admin_id:
            users = User.objects.all()
            serializer = AdminSerializer(users, many=True)
            return Response(serializer.data, status.HTTP_200_OK)

        user = User.objects.filter(user_id=admin_id)

        if not user.exists():
            return Response({"error": "Admin not found"}, status.HTTP_404_NOT_FOUND)

        serializer = AdminSerializer(user.first())

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, admin_id):

        user = User.objects.filter(user_id=admin_id)

        serializer = AdminSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data.get("password"):
            serializer.validated_data["password"] = make_password(
                serializer.validated_data["password"]
            )

        try:
            user.update(**serializer.validated_data)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)

        user: User = user.first()

        serializer = AdminSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, _, admin_id):

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

        found_guest = User.objects.filter(
            email=serializer.validated_data["email"]
        ).exists()

        if found_guest:
            return Response({"error": "Guest already exists"}, status.HTTP_409_CONFLICT)

        guest: User = User.objects.create(**serializer.validated_data)
        guest.set_password(serializer.validated_data["password"])
        guest.save()

        serializer = GuestsSerializer(guest)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, request, guest_id):

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
                return Response({"error": "Email already exists."}, status.HTTP_409_CONFLICT)


class UsersView(APIView):
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

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
