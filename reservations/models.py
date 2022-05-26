from uuid import uuid4

from django.db import models


class Reservation(models.Model):
    reservation_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    in_reservation = models.DateField()
    out_reservation = models.DateField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    status = models.CharField(max_length=50)

    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reservations"
    )
    room_category = models.ForeignKey(
        "room_categories.RoomCategory", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="reservations"
    )
