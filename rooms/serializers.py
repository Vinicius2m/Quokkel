from rest_framework import serializers

from room_categories.serializers import RoomCategorySerializer


class RoomsSerializer(serializers.Serializer):
    room_id = serializers.UUIDField(read_only=True)
    number = serializers.IntegerField()
    available = serializers.BooleanField()

    room_category = RoomCategorySerializer(many=False, required=False)
