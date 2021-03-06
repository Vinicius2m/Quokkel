from rest_framework import serializers

from room_categories.serializers import RoomCategoriesSerializer
from rooms.serializers import RoomSerializer
from users.serializers import GuestsSerializer


class ReservationsSerializer(serializers.Serializer):
    reservation_id = serializers.UUIDField(read_only=True)
    in_reservation_date = serializers.DateField(required=True)
    out_reservation_date = serializers.DateField(required=True)
    status = serializers.CharField(required=False)
    total_value = serializers.DecimalField(
        required=False, max_digits=10, decimal_places=2, coerce_to_string=False
    )
    guest_email = serializers.EmailField(write_only=True)


class ReservationsDataSerializer(serializers.Serializer):
    reservation_id = serializers.UUIDField(read_only=True)
    in_reservation_date = serializers.DateField(required=True)
    out_reservation_date = serializers.DateField(required=True)
    checkin_date = serializers.DateField(required=False)
    checkout_date = serializers.DateField(required=False)
    status = serializers.CharField(required=True)
    total_value = serializers.DecimalField(
        required=False, max_digits=10, decimal_places=2, coerce_to_string=False
    )
    guest_id = (GuestsSerializer(),)
    room_category = RoomCategoriesSerializer(required=False)
    room = RoomSerializer(required=False)


class RetreiveReservationsSerializer(serializers.Serializer):
    reservation_id = serializers.UUIDField(read_only=True)
    in_reservation_date = serializers.DateField(required=True)
    out_reservation_date = serializers.DateField(required=True)
    checkin_date = serializers.DateField(required=False)
    checkout_date = serializers.DateField(required=False)
    status = serializers.CharField(required=True)
    total_value = serializers.DecimalField(
        required=False, max_digits=10, decimal_places=2, coerce_to_string=False
    )
    guest = GuestsSerializer()
    room = RoomSerializer(required=False)
    room_category = RoomCategoriesSerializer(required=False)


class CheckinReservationSerializer(serializers.Serializer):
    checkin_date = serializers.DateField(required=True)


class CheckoutReservationSerializer(serializers.Serializer):
    checkout_date = serializers.DateField(required=True)


class UpdateReservationsSerializer(serializers.Serializer):
    reservation_id = serializers.UUIDField(read_only=True)
    in_reservation_date = serializers.DateField(required=False)
    out_reservation_date = serializers.DateField(required=False)
    status = serializers.CharField(required=False)
    total_value = serializers.DecimalField(
        required=False, max_digits=10, decimal_places=2, coerce_to_string=False
    )
