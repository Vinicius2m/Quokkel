from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
                                   HTTP_409_CONFLICT)
from rest_framework.views import APIView

from room_categories.models import RoomCategory
from users.models import User

from .models import Reservation
from .serializers import ReservationsDataSerializer, ReservationsSerializer


class ReservationsView(APIView):
    def post(self, request: Request, room_category_id: str = ""):
        serializer = ReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        filtered_guest = User.objects.filter(
            email=serializer.validated_data["guest"]
        ).first()
        conflicting_reservation = Reservation.objects.filter(
            in_reservation_date=request.data["in_reservation_date"]
        ).first()

        if conflicting_reservation:
            return Response(
                {"error": "Reservation unavailable"}, status=HTTP_409_CONFLICT
            )

        if not filtered_guest:
            return Response(
                {"error": "Guest does not exist, please register it"},
                status=HTTP_400_BAD_REQUEST,
            )

        if len(room_category_id) == 0:
            return Response(
                {"error": "Room category id is required"}, status=HTTP_400_BAD_REQUEST
            )

        reservation_data = {
            "in_reservation_date": request.data["in_reservation_date"],
            "out_reservation_date": request.data["out_reservation_date"],
            "checkin_date": request.data["checkin_date"],
            "checkout_date": request.data["checkout_date"],
            "status": request.data["status"],
            "total_value": request.data["total_value"],
            "guest_id": filtered_guest.__dict__["user_id"],
            "room_category_id": room_category_id,
        }

        reservation = Reservation.objects.create(**reservation_data)
        serializer = ReservationsDataSerializer(reservation)

        if not reservation:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=HTTP_201_CREATED)
