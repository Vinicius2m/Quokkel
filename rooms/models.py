from uuid import uuid4

from django.db import models


class Room(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    number = models.IntegerField(null=False)
    available = models.BooleanField(default=True)

    room_category = models.ForeignKey(
        "room_categories.RoomCategory", on_delete=models.CASCADE
    )
