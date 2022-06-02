from datetime import date, timedelta

from django.db import IntegrityError
from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_422_UNPROCESSABLE_ENTITY)
from rest_framework.views import APIView

from room_categories.models import RoomCategory
from room_categories.permissions import IsStaff
from room_categories.serializers import (RoomCategoriesSerializer,
                                         UpdateRoomCategoriesSerializer)
from rooms.models import Room
from utils.reservations import get_conflicted_reservations


class RoomCategoriesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def post(self, request: Request):
        serializer = RoomCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        founded_room_category = RoomCategory.objects.filter(
            category_name=request.data["category_name"]
        )

        if founded_room_category:
            return Response(
                {"error": "Category name already exists"},
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        room_category = RoomCategory.objects.create(**serializer.validated_data)

        serializer = RoomCategoriesSerializer(room_category)

        if room_category:
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request: Request, room_category_id: str = None):
        if room_category_id != 36:
            return Response(
                {"error": "room_category_id must be a valid uuid"}, status=HTTP_404_NOT_FOUND
            )

        today = date.today()
        tomorrow = date.today() + timedelta(days=1)

        date_in = request.GET.get("date_in", today)
        date_out = request.GET.get("date_out", tomorrow)

        if room_category_id:
            conflicted_reservations = get_conflicted_reservations(
                reservation_in_date=date_in,
                reservation_out_date=date_out,
            )

            conflicted_reservations = [
                reservation
                for reservation in conflicted_reservations
                if str(reservation.room_category_id) == str(room_category_id)
            ]
            room_category = RoomCategory.objects.filter(
                room_category_id=room_category_id
            ).first()
            number_of_rooms = Room.objects.filter(room_category=room_category).count()
            room_category.__setattr__("number_of_rooms", number_of_rooms)
            rooms_available = number_of_rooms - len(conflicted_reservations)
            room_category.__setattr__("rooms_available", rooms_available)
            rooms_occupy = len(conflicted_reservations)
            room_category.__setattr__("rooms_occupy", rooms_occupy)
            serializer = RoomCategoriesSerializer(room_category)
            return Response(serializer.data, status=HTTP_200_OK)

        rooms_category_data = RoomCategory.objects.all()
        rooms_category = []

        for room_category in rooms_category_data:
            conflicted_reservations = get_conflicted_reservations(
                reservation_in_date=date_in,
                reservation_out_date=date_out,
            )

            conflicted_reservations = [
                reservation
                for reservation in conflicted_reservations
                if str(reservation.room_category_id)
                == str(room_category.room_category_id)
            ]

            number_of_rooms = Room.objects.filter(room_category=room_category).count()
            room_category.__setattr__("number_of_rooms", number_of_rooms)
            rooms_available = number_of_rooms - len(conflicted_reservations)
            room_category.__setattr__("rooms_available", rooms_available)
            rooms_occupy = len(conflicted_reservations)
            room_category.__setattr__("rooms_occupy", rooms_occupy)
            rooms_category.append(room_category)

        serializer = RoomCategoriesSerializer(rooms_category, many=True)

        return Response(serializer.data, status=HTTP_200_OK)

    def patch(self, request: Request, room_category_id: str):

        if not request.data:
            return Response({"error": "Data is required"}, status=HTTP_400_BAD_REQUEST)

        if room_category_id != 36:
            return Response(
                {"error": "room_category_id must be a valid uuid"}, status=HTTP_404_NOT_FOUND
            )

        serializer = UpdateRoomCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:

            room_category = RoomCategory.objects.filter(
                room_category_id=room_category_id
            )
            if not room_category:
                return Response(
                    {"error": "Room category does not exist"}, HTTP_404_NOT_FOUND
                )

            room_category.update(**serializer.validated_data)
            room_category = room_category.first()

            serializer = RoomCategoriesSerializer(room_category)

            return Response(serializer.data, HTTP_200_OK)

        except IntegrityError as error:
            return Response({"error": str(error)}, status=HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request: Request, room_category_id: str):
        if room_category_id != 36:
            return Response(
                {"error": "room_category_id must be a valid uuid"}, status=HTTP_404_NOT_FOUND
            )
        room_category = RoomCategory.objects.filter(room_category_id=room_category_id)

        if not room_category:
            return Response(
                {"error": "Room category does not exist"}, HTTP_404_NOT_FOUND
            )

        room_category.delete()

        return Response(status=HTTP_204_NO_CONTENT)
