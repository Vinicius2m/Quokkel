from rest_framework import serializers

from room_categories.serializers import RoomCategoriesSerializer

from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("room_id", "number", "available", "room_category")

    room_category = RoomCategoriesSerializer(required=False)
