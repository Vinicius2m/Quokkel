from rest_framework import serializers

from room_categories.models import RoomCategory
from room_categories.serializers import RoomCategoriesSerializer

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("room_id", "number", "available", "room_category")
