from django.db import IntegrityError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,
                                   HTTP_422_UNPROCESSABLE_ENTITY)
from rest_framework.views import APIView

from .models import RoomCategory
from .serializers import (RoomCategoriesSerializer,
                          UpdateRoomCategoriesSerializer)


class RoomCategoriesView(APIView):
    def post(self, request: Request):
        serializer = RoomCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        founded_room_category = RoomCategory.objects.filter(
            category_name=request.data["category_name"]
        )

        if founded_room_category:
            return Response(
                {"error": "Category name already exists"},
                status=HTTP_422_UNPROCESSABLE_ENTITY,
            )

        room_category = RoomCategory.objects.create(**serializer.validated_data)

        serializer = RoomCategoriesSerializer(room_category)

        if room_category:
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request: Request, room_category_id: str = None):

        if room_category_id:
            room_category = RoomCategory.objects.filter(
                room_category_id=room_category_id
            ).first()
            serializer = RoomCategoriesSerializer(room_category)
            return Response(serializer.data, status=HTTP_200_OK)

        rooms_category = RoomCategory.objects.all()

        serializer = RoomCategoriesSerializer(rooms_category, many=True)

        return Response(serializer.data, status=HTTP_200_OK)

    def patch(self, request: Request, room_category_id: str):
        serializer = UpdateRoomCategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:

            room_category = RoomCategory.objects.filter(
                room_category_id=room_category_id
            )
            if not room_category:
                return Response(
                    {"error": "Room category does not exist"}, HTTP_404_NOT_FOUND
                )

            room_category.update(**serializer.validated_data)
            room_category = room_category.first()

            serializer = RoomCategoriesSerializer(room_category)

            return Response(serializer.data, HTTP_200_OK)

        except IntegrityError as error:
            return Response({"error": str(error)}, status=HTTP_422_UNPROCESSABLE_ENTITY)
