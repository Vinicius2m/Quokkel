from rest_framework import serializers


class RoomCategoriesSerializer(serializers.Serializer):
    room_category_id = serializers.UUIDField(read_only=True)
    category_name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_guest_number = serializers.IntegerField()

    number_of_rooms = serializers.IntegerField(read_only=True)


class UpdateRoomCategoriesSerializer(serializers.Serializer):
    room_category_id = serializers.UUIDField(read_only=True)
    category_name = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    max_guest_number = serializers.IntegerField(required=False)

    number_of_rooms = serializers.IntegerField(read_only=True)
