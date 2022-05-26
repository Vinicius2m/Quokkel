from rest_framework import serializers


class RoomCategorySerializer(serializers.Serializer):
    room_category_id = serializers.UUIDField(read_only=True)
    category_name = serializers.CharField()
    price = serializers.DecimalField()
    max_guest_number = serializers.IntegerField()

    number_of_rooms = serializers.IntegerField(read_only=True)


class UpdateRoomCategorySerializer(serializers.Serializer):
    room_category_id = serializers.UUIDField(read_only=True)
    category_name = serializers.CharField(null=True)
    price = serializers.DecimalField(null=True)
    max_guest_number = serializers.IntegerField(null=True)

    number_of_rooms = serializers.IntegerField(read_only=True)
