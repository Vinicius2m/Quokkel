from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_409_CONFLICT,
    HTTP_201_CREATED,
)

from .serializers import ReservationsSerializer
from .models import Reservation


class ReservationsView(APIView):
    def post(self, request: Request):
        serializer = ReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        conflicting_reservation = Reservation.objects.filter(
            in_reservation_date=request.data["in_reservation_date"]
        ).first()

        if conflicting_reservation:
            return Response(
                {"error": "Reservation unavailable"}, status=HTTP_409_CONFLICT
            )

        reservation = Reservation.objects.create(**serializer.validated_data)
        serializer = ReservationsSerializer(reservation)

        if not reservation:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=HTTP_201_CREATED)
