from uuid import uuid4

from django.db import models


class RoomCategory(models.Model):
    room_category_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    category_name = models.CharField(max_length=150, unique=True, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    max_guest_number = models.IntegerField(null=False)
