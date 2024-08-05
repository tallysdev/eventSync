from core.models import ThemeRoom
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import ReadOnly
from ..serializers.theme_room_serializers import ThemeRoomSerializer


class ThemeRoomListView(APIView):
    """
    List all Themes Rooms, or create a new Theme Room.
    """
    # permission_classes = [IsAuthenticated | ReadOnly]  
    pagination_class = PageNumberPagination

    @extend_schema(
        responses={200: ThemeRoomSerializer(many=True)},
        parameters=[
            OpenApiParameter(name='page', description='Page number', required=False, type=int),
            OpenApiParameter(name='page_size', description='Page size', required=False, type=int),
        ], 
    )

    def get(self, request, format=None):
        themeRoom = ThemeRoom.objects.all().order_by("id")
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(themeRoom, request)
        serializer = ThemeRoomSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    @extend_schema(
        request=ThemeRoomSerializer,
        responses={201: ThemeRoomSerializer},
    )
    def post(self, request, format=None):
        # print("oi lucas", request.data)
        serializer = ThemeRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThemeRoomDetailView(APIView):
    """
    Retrieve, update or delete an Theme Room.
    """
    permission_classes = [IsAuthenticated | ReadOnly]

    def get_object(self, pk):
        try:
            return ThemeRoom.objects.get(pk=pk)
        except ThemeRoom.DoesNotExist:
            raise Http404

    @extend_schema(
        responses={200: ThemeRoomSerializer},
    )
    def get(self, request, pk, format=None):
        themeRoom = self.get_object(pk)
        serializer = ThemeRoomSerializer(themeRoom)
        return Response(serializer.data)

    @extend_schema(
        request=ThemeRoomSerializer,
        responses={200: ThemeRoomSerializer},
    )
    def patch(self, request, pk, format=None):
        themeRoom = self.get_object(pk)
        serializer = ThemeRoomSerializer(themeRoom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={204: None},
    )
    def delete(self, request, pk, format=None):
        themeRoom = self.get_object(pk)
        themeRoom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
