from django.core.exceptions import BadRequest
from django.db import IntegrityError
from django.forms import ValidationError
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
)
from rest_framework.views import APIView

from reservations.models import Reservation
from reservations.serializers import (
    ReservationsDataSerializer,
    ReservationsSerializer,
    RetreiveReservationsSerializer,
    UpdateReservationsSerializer,
)
from users.models import User
from users.permissions import IsStaff


class ReservationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, room_category_id: str = ""):
        serializer = ReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            filtered_guest = User.objects.filter(
                email=serializer.validated_data["guest"]
            ).first()

            conflicting_reservation = Reservation.objects.filter(
                in_reservation_date=request.data["in_reservation_date"]
            ).first()

            if conflicting_reservation:
                raise ValidationError("Reservation unavailable")

            if len(room_category_id) == 0:
                raise BadRequest("Please provide a room category")

            if not filtered_guest:
                raise BadRequest("Guest does not exist")

            reservation_data = {
                "in_reservation_date": request.data["in_reservation_date"],
                "out_reservation_date": request.data["out_reservation_date"],
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
        except ValidationError as error:
            return Response({"error": error.message}, status=HTTP_409_CONFLICT)
        except BadRequest as error:
            return Response({"error": str(error)}, status=HTTP_400_BAD_REQUEST)

    def get(self, _: Request, guest_id: str = None):
        if not guest_id:
            reservations = list(Reservation.objects.all())

            for reservation in reservations:
                reservation.guest = User.objects.filter(
                    user_id=reservation.guest_id
                ).first()

            serializer = RetreiveReservationsSerializer(reservations, many=True)
        else:
            reservations = Reservation.objects.filter(guest_id=guest_id)

            serializer = ReservationsDataSerializer(reservations, many=True)

        return Response(serializer.data, status=HTTP_200_OK)


class DeleteReservationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def delete(self, _: Request, reservation_id: str):
        if not reservation_id:
            return Response(
                {"error": "Reservation does not exist"}, status=HTTP_404_NOT_FOUND
            )

        try:
            reservation = Reservation.objects.get(reservation_id=reservation_id)
            reservation.delete()

            return Response(status=HTTP_204_NO_CONTENT)
        except Reservation.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


class RetrieveReservationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _: Request, reservation_id: str):
        reservation = Reservation.objects.filter(reservation_id=reservation_id).first()

        if not reservation:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = RetreiveReservationsSerializer(reservation)

        return Response(serializer.data, status=HTTP_200_OK)


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
