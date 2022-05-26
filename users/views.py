from django.shortcuts import render
from django.contrib.auth.hashers import check_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.models import User
from users.serializers import AdminSerializer, GuestsSerializer, LoginSerializer


class AdminView(APIView):
    def post(self, request):

        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_user = User.objects.filter(
            email=serializer.validated_data["email"]
        ).first()

        if found_user:
            return Response(
                {"error": "User already exists"}, status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        user: User = User.objects.create(**serializer.validated_data)
        user.set_password(serializer.validated_data["password"])
        user.save()

        serializer = UsersSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class GuestsView(APIView):
    def post(self, request):

        serializer = GuestsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

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


class UsersView(APIView):
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: User = User.objects.filter(
            email=serializer.validated_data["email"]
        ).first()

        if not check_password(serializer.validated_data["password"], user.password):
            return Response(
                {"error": "Invalid credentials."}, status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status.HTTP_200_OK)
