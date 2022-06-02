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
    CheckinReservationSerializer,
    CheckoutReservationSerializer,
    ReservationsDataSerializer,
    ReservationsSerializer,
    RetreiveReservationsSerializer,
    UpdateReservationsSerializer,
)
from room_categories.models import RoomCategory
from rooms.models import Room
from users.models import User
from users.permissions import IsStaff
from utils.reservations import get_conflicted_reservations


class ReservationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, room_category_id: str = ""):
        serializer = ReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            filtered_guest = User.objects.filter(
                email=serializer.validated_data["guest_email"]
            ).first()

            if not room_category_id:
                raise BadRequest("Please provide a room category")

            if not filtered_guest:
                raise BadRequest("Guest does not exist")

            # Obter lista das reservas com datas conflitantes
            conflicted_reservations = get_conflicted_reservations(
                reservation_in_date=serializer.validated_data["in_reservation_date"],
                reservation_out_date=serializer.validated_data["out_reservation_date"],
            )

            # Filtrar conflito por categoria de quarto
            conflicted_reservations = [
                reservation
                for reservation in conflicted_reservations
                if str(reservation.room_category_id) == str(room_category_id)
            ]

            rooms_quantity = Room.objects.filter(room_category=room_category_id).count()

            if not rooms_quantity:
                raise BadRequest("There are no rooms available for this category")

            if rooms_quantity <= len(conflicted_reservations):
                raise BadRequest(
                    f"There's not available rooms for this category between {serializer.validated_data['in_reservation_date']} and {serializer.validated_data['out_reservation_date']}"
                )

            reservation_data = {
                "in_reservation_date": request.data["in_reservation_date"],
                "out_reservation_date": request.data["out_reservation_date"],
                "status": "reserved",
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
        except TypeError as error:
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

        serializer = UpdateReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reservation = Reservation.objects.filter(reservation_id=reservation_id)

        if not reservation.first():
            return Response(
                {"error": "Reservation not found"}, status=HTTP_404_NOT_FOUND
            )

        if serializer.validated_data.get("status") and serializer.validated_data.get(
            "status"
        ) not in [
            "reserved",
            "occupied",
            "closed",
        ]:
            return Response(
                {"error": "Invalid status - (reserved, occupied, closed)"},
                status=HTTP_400_BAD_REQUEST,
            )

        room_category_id = reservation.first().room_category.room_category_id

        # Obter lista das reservas com datas conflitantes
        conflicted_reservations = get_conflicted_reservations(
            reservation_in_date=request.data.get(
                "in_reservation_date", reservation.first().in_reservation_date
            ),
            reservation_out_date=request.data.get(
                "out_reservation_date", reservation.first().out_reservation_date
            ),
            reservation_id=reservation_id,
        )

        # Filtrar conflito por categoria de quarto
        conflicted_reservations = [
            reservation
            for reservation in conflicted_reservations
            if str(reservation.room_category_id) == str(room_category_id)
        ]

        rooms_quantity = Room.objects.filter(room_category=room_category_id).count()

        if rooms_quantity <= len(conflicted_reservations):
            return Response(
                {
                    "message": f"There's not available rooms for this category between {serializer.validated_data['in_reservation_date']} and {serializer.validated_data['out_reservation_date']}"
                },
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            reservation.update(**serializer.validated_data)
        except IntegrityError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

        reservation = reservation.first()

        serializer = ReservationsDataSerializer(reservation)

        return Response(serializer.data, status=HTTP_200_OK)


class CheckinReservationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def put(self, request: Request, reservation_id):

        serializer = CheckinReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            reservation: Reservation = Reservation.objects.filter(
                reservation_id=reservation_id
            )

            if not reservation:
                return Response(
                    {"error": "Reservation not found"}, status=HTTP_404_NOT_FOUND
                )

            checkin_date = reservation.first().checkin_date

            if checkin_date:
                return Response(
                    {"error": "Checkin already exists"}, status=HTTP_409_CONFLICT
                )

            room_category_id = reservation.first().room_category.room_category_id

            rooms = Room.objects.filter(room_category_id=room_category_id).all()
            print(rooms)

            room_id = [room.room_id for room in rooms if room.available == True][0]

            Room.objects.filter(room_id=room_id).update(**{"available": False})

            serializer.validated_data["room"] = room_id
            serializer.validated_data["status"] = "occupied"

            reservation.update(**serializer.validated_data)

            reservation: Reservation = reservation.first()

            serializer = RetreiveReservationsSerializer(reservation)

            return Response(serializer.data, status=HTTP_200_OK)

        except ValidationError as error:
            return Response({"error": error}, status=HTTP_400_BAD_REQUEST)


class CheckoutReservationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def put(self, request: Request, reservation_id):

        serializer = CheckoutReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            reservation: Reservation = Reservation.objects.filter(
                reservation_id=reservation_id
            )

            if not reservation:
                return Response(
                    {"error": "Reservation not found"}, status=HTTP_404_NOT_FOUND
                )

            reservation_dict = reservation.first()

            checkin_date = reservation_dict.checkin_date
            checkout_date = serializer.validated_data.get("checkout_date")

            if reservation_dict.checkout_date:
                return Response(
                    {"error": "Reservation already checked out"},
                    status=HTTP_409_CONFLICT
                )

            number_of_days = abs((checkout_date - checkin_date).days) + 1

            room_category_price = (
                RoomCategory.objects.filter(
                    room_category_id=reservation_dict.room_category_id
                )
                .first()
                .price
            )

            serializer.validated_data["total_value"] = (
                number_of_days * room_category_price
            )

            Room.objects.filter(room_id=reservation_dict.room_id).update(
                **{"available": True}
            )

            serializer.validated_data["status"] = "closed"
            serializer.validated_data["room"] = None

            reservation.update(**serializer.validated_data)

            reservation: Reservation = reservation.first()

            serializer = RetreiveReservationsSerializer(reservation)

            return Response(serializer.data, status=HTTP_200_OK)

        except ValidationError as error:
            return Response({"error": error}, status=HTTP_400_BAD_REQUEST)
        except TypeError as error:
            return Response(
                {"error": error},
                status=HTTP_400_BAD_REQUEST,
            )
