from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from room_categories.models import RoomCategory
from rooms.models import Room
from rooms.serializers import RoomSerializer


class RoomView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def post(self, request, room_category_id):
        room_category = RoomCategory.objects.filter(
            room_category_id=room_category_id
        ).first()
        if not room_category:
            return Response({"error": "Room category not found"}, status=404)
        rooms_data = request.data
        rooms_data["room_category"] = room_category.room_category_id
        serializer = RoomSerializer(data=rooms_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"
    lookup_field = "room_id"
