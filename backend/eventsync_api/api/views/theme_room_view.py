from core.models import ThemeRoom, Event
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import ReadOnly
from ..serializers.theme_room_serializers import ThemeRoomSerializer
from datetime import date


class ThemeRoomListView(APIView):
    """
    List all Theme Rooms for a specific Event, or create a new Theme Room for that Event.
    """
    # permission_classes = [IsAuthenticated | ReadOnly]

    @extend_schema(
        responses={200: ThemeRoomSerializer(many=True)},
        parameters=[
            OpenApiParameter(name='event_id', description='Event ID', required=True, type=int),

            OpenApiParameter(name='page', description='Page number', required=False, type=int),

            OpenApiParameter(name='page_size', description='Page size', required=False, type=int),
        ],
    )
    def get(self, request, format=None):
        # Obtenha o ID do evento da query string
        event_id = request.query_params.get('event_id')

        if not event_id:
            return Response({"detail": "Event ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Filtrar as Theme Rooms pelo evento específico
        theme_rooms = ThemeRoom.objects.filter(event__id=event_id).order_by("id")

        # Serializar os dados
        serializer = ThemeRoomSerializer(theme_rooms, many=True)

        return Response(serializer.data)

    @extend_schema(
        request=ThemeRoomSerializer,

        responses={201: ThemeRoomSerializer},
    )
    def post(self, request, format=None):
        # Obtenha o ID do evento do corpo da requisição
        event_id = request.data.get('event')

        # if not event_id:
        #     return Response({"detail": "Event ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Busque o evento pelo ID
            event = Event.objects.get(id=event_id)

        except Event.DoesNotExist:

            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        # Obtenha as datas do evento
        event_start_date = event.start_date

        event_end_date = event.end_date

        # Obtenha a data de início e fim da Theme Room
        theme_room_start_date = request.data.get('start_date')

        theme_room_end_date = request.data.get('end_date')

        # Valide se as datas da Theme Room estão dentro do intervalo do evento
        if theme_room_start_date and theme_room_end_date:

            # Converta as datas para objetos date, se necessário
            theme_room_start_date = date.fromisoformat(theme_room_start_date)

            theme_room_end_date = date.fromisoformat(theme_room_end_date)

            if theme_room_start_date < event_start_date or theme_room_end_date > event_end_date:
                return Response(
                    {"detail": "Theme room dates must be within the event's date range."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Serializar e salvar os dados
        serializer = ThemeRoomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ThemeRoomDetailView(APIView):
    """
    Retrieve, update or delete a Theme Room.
    """
    # permission_classes = [IsAuthenticated | ReadOnly]

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
        
        # Obtenha o evento associado a esta Theme Room
        event = themeRoom.event
        
        # Obtenha as datas do evento
        event_start_date = event.start_date

        event_end_date = event.end_date

        # Obtenha a data de início e fim da Theme Room do request
        theme_room_start_date = request.data.get('start_date', themeRoom.start_date)

        theme_room_end_date = request.data.get('end_date', themeRoom.end_date)

        # Valide se as novas datas da Theme Room estão dentro do intervalo do evento
        if theme_room_start_date and theme_room_end_date:
            # Converta as datas para objetos date, se necessário
            theme_room_start_date = date.fromisoformat(theme_room_start_date) if isinstance(theme_room_start_date, str) else theme_room_start_date
            
            theme_room_end_date = date.fromisoformat(theme_room_end_date) if isinstance(theme_room_end_date, str) else theme_room_end_date

            if theme_room_start_date < event_start_date or theme_room_end_date > event_end_date:
                return Response(
                    {"detail": "Theme room dates must be within the event's date range."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Atualize a Theme Room com os dados do request
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