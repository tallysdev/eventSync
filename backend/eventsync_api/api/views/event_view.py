from core.models import Event
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import IsOrganizerOrReadOnly
from ..serializers.event_serializers import EventSerializer

from ..utils.register import save_current_user_registration

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class EventListView(APIView):
    """
    List all events, or create a new event.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination

    @extend_schema(
        responses={200: EventSerializer(many=True)},
        parameters=[
            OpenApiParameter(name='page', description='Page number', required=False, type=int),
            OpenApiParameter(name='page_size', description='Page size', required=False, type=int),
            OpenApiParameter(name='status', description='Event status', required=False, type=str),
            OpenApiParameter(name='event_type', description='Event type', required=False, type=str),
            OpenApiParameter(name='name', description='Event name', required=False, type=str),
        ],
    )
    def get(self, request, format=None):
        events = Event.objects.all().order_by("id")

        # Filter by status if the status parameter is provided
        status_filter = request.query_params.get('status')
        if status_filter:
            events = events.filter(status=status_filter)

        # Filter by event type if the event_type parameter is provided
        event_type_filter = request.query_params.get('event_type')
        if event_type_filter:
            events = events.filter(event_type=event_type_filter)

        # Filter by name if the name parameter is provided
        name_filter = request.query_params.get('name')
        if name_filter:
            events = events.filter(name__icontains=name_filter)

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(events, request)
        serializer = EventSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(
        request=EventSerializer,
        responses={201: EventSerializer},
    )
    def post(self, request, format=None):
        print(request.user)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event_instance = serializer.save()  # Salva o evento
            save_current_user_registration(request.user, event_instance)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    """
    Retrieve, update or delete an event.
    """
    permission_classes = [IsOrganizerOrReadOnly]

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
