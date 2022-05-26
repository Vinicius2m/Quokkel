from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsStaff
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


class GuestsView(APIView):
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
