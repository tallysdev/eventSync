from core.models import EventRegistration, Event, ESUser
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.event_registration_serializers import EventRegistrationSerializer


class EventSignupView(APIView):
    """
    Handle user signup to an event.
    """
    permission_classes = [IsAuthenticated]


    @extend_schema(
        request=EventRegistrationSerializer,
        responses={201: EventRegistrationSerializer},
        parameters=[
            OpenApiParameter(name='event_id', description='Event ID', required=True, type=int),
            OpenApiParameter(name='user_id', description='User ID', required=True, type=int),
        ]
    )
    def post(self, request, format=None):
        event_id = request.query_params.get('event_id')
        user_id = request.query_params.get('user_id')

        event = Event.objects.get(id=event_id)
        user = ESUser.objects.get(id=user_id)

        data = {'user': user.id, 'event': event.id}

        serializer = EventRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
