from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from room_categories.models import RoomCategory
from rooms.models import Room
from rooms.serializers import RoomSerializer

from rooms.permissions import IsStaff


class RoomView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def post(self, request, room_category_id):
        room_category = RoomCategory.objects.filter(
            room_category_id=room_category_id
        ).first()
        if not room_category:
            return Response(
                {"error": "Room category not found"}, status=status.HTTP_404_NOT_FOUND
            )

        rooms_data = request.data
        serializer = RoomSerializer(data=rooms_data)
        if serializer.is_valid():
            serializer.validated_data["room_category"] = room_category
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "room_id"
    lookup_field = "room_id"


class RoomStatusView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaff]

    def get(self, request, room_category_id):

        rooms = Room.objects.filter(room_category_id=room_category_id).all()

        available = request.GET.get("available", None)

        if available:
            if available == "true":
                rooms = rooms.filter(available=True)
            elif available == "false":
                rooms = rooms.filter(available=False)

        serializer = RoomSerializer(rooms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
