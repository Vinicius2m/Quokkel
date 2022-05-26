from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_422_UNPROCESSABLE_ENTITY
)

from .serializers import RoomCategoriesSerializer, UpdateRoomCategoriesSerializer
from .models import RoomCategory

class RoomCategoriesView(APIView):
    def post(self, request: Request):
        serializer = RoomCategoriesSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        founded_room_category = RoomCategory.objects.filter(category_name=request.data['category_name'])

        if founded_room_category:
            return Response({'error': 'Category name already exists'}, status=HTTP_422_UNPROCESSABLE_ENTITY)

        room_category = RoomCategory.objects.create(**serializer.validated_data)

        serializer = RoomCategoriesSerializer(room_category)

        if room_category:
            return Response(serializer.data, status=HTTP_201_CREATED)


        return Response(
            data=serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
    