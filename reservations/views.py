from django.db import IntegrityError
from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
)
from rest_framework.views import APIView

from reservations.models import Reservation
from reservations.serializers import (
    ReservationsDataSerializer,
    ReservationsSerializer,
    UpdateReservationsSerializer,
)
from users.models import User
from users.permissions import IsStaff


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


class UpdateReservationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def patch(self, request: Request, reservation_id):
        if not request.data:
            return Response({"error": "Data is required"}, status=HTTP_400_BAD_REQUEST)

        reservation = Reservation.objects.filter(reservation_id=reservation_id)

        if not reservation.first():
            return Response(
                {"error": "Reservation not found"}, status=HTTP_404_NOT_FOUND
            )

        serializer = UpdateReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            reservation.update(**serializer.validated_data)
        except IntegrityError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

        reservation = reservation.first()

        serializer = ReservationsDataSerializer(reservation)

        return Response(serializer.data, status=HTTP_200_OK)
