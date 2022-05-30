from uuid import uuid4

from django.db import models


class Reservation(models.Model):
    reservation_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    in_reservation_date = models.DateField()
    out_reservation_date = models.DateField()
    checkin_date = models.DateField(null=True, blank=True)
    checkout_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reservations"
    )
    room_category = models.ForeignKey(
        "room_categories.RoomCategory", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="reservations", null=True
    )
