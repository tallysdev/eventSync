from core.models import RegistrationPresence, Event, ESUser
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.registration_presence_serializers import RegistrationPresenceSerializer


class RegistrationPresence(APIView):
    """
    Handle user signup to an event.
    """
    permission_classes = [IsAuthenticated]


    @extend_schema(
        request=RegistrationPresenceSerializer,
        responses={201: RegistrationPresenceSerializer},
        parameters=[
            OpenApiParameter(name='event_id', description='Event ID', required=True, type=int),
            OpenApiParameter(name='user_id', description='User ID', required=True, type=int),
        ]
    )
    def post(self, request, format=None):
        event_id = request.query_params.get('event_id')
        user_id = request.query_params.get('user_id')

        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = ESUser.objects.get(id=user_id)
        except ESUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'user': user.id,
            'event': event.id,
        }

        serializer = RegistrationPresenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
