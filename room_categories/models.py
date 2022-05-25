from uuid import uuid4

from django.db import models


class RoomCategory(models.Model):
    room_category_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    category_name = models.CharField(max_length=255, unique=True, null=False)
    price = models.FloatField(null=False)
    max_guest_number = models.IntegerField(null=False)

    reservations = models.ForeignKey(
        "reservations.Reservation",
        on_delete=models.CASCADE,
        related_name="room_category",
        null=False,
    )
