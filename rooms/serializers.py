from rest_framework import serializers

from room_categories.serializers import RoomCategoriesSerializer


class RoomsSerializer(serializers.Serializer):
    room_id = serializers.UUIDField(read_only=True)
    number = serializers.IntegerField(required=True)
    available = serializers.BooleanField()

    room_category = RoomCategoriesSerializer(many=False, required=False)
