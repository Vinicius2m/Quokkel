from django.shortcuts import render
from rest_framework.views import APIView
from users.models import User

from users.serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status


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
        serializer = UsersSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
