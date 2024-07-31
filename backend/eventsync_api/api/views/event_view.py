from core.models import Event
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import ReadOnly
from ..serializers.event_serializers import EventSerializer


class EventListView(APIView):
    """
    List all events, or create a new event.
    """
    # permission_classes = [IsAuthenticated | ReadOnly]
    pagination_class = PageNumberPagination

    @extend_schema(
        responses={200: EventSerializer(many=True)},
        parameters=[
            OpenApiParameter(name='page', description='Page number', required=False, type=int),
            OpenApiParameter(name='page_size', description='Page size', required=False, type=int),
        ],
    )
    def get(self, request, format=None):
        events = Event.objects.all().order_by("id")
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(events, request)
        serializer = EventSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(
        request=EventSerializer,
        responses={201: EventSerializer},
    )
    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    """
    Retrieve, update or delete an event.
    """
 #   permission_classes = [IsAuthenticated | ReadOnly]

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    @extend_schema(
        responses={200: EventSerializer},
    )
    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @extend_schema(
        request=EventSerializer,
        responses={200: EventSerializer},
    )
    def patch(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={204: None},
    )
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
