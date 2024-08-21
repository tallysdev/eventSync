from core.models import ESUser, Event, RegistrationPresence
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsOrganizerForPatch, ReadOnly
from ..serializers.registration_presence_serializers import \
    RegistrationPresenceSerializer

from ..serializers.auth_serializers import ESUserSerializer


class RegistrationPresenceList(APIView):
    """
    Handle user signup to an event.
    """
    permission_classes = [IsAuthenticated | ReadOnly]
    pagination_class = PageNumberPagination

    @extend_schema(
        request=RegistrationPresenceSerializer,
        responses={201: RegistrationPresenceSerializer},
        parameters=[
            OpenApiParameter(name='event_id', description='Event ID', required=True, type=int),
            OpenApiParameter(name='user_id', description='User ID', required=True, type=int),
        ]
    )
    def post(self, request, format=None):
        print(request.user)
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


class RegistrationPresenceDetail(APIView):
    """
    Handle retrieving and deleting a specific registration for an event.
    """
    permission_classes = [IsOrganizerForPatch,]

    def get_object(self, event, user):
        try:
            return RegistrationPresence.objects.get(event=event, user=user)
        except RegistrationPresence.DoesNotExist:
            raise Http404

    @extend_schema(
        summary='Retrieve a registration presence',
        responses={200: RegistrationPresenceSerializer},
    )
    def get(self, request, event_id, user_id, format=None):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = ESUser.objects.get(id=user_id)
        except ESUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        registration = self.get_object(event, user)
        serializer = RegistrationPresenceSerializer(registration)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary='Update a registration presence',
        request=RegistrationPresenceSerializer,
        responses={200: RegistrationPresenceSerializer},
    )
    def patch(self, request, event_id, user_id, format=None):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = ESUser.objects.get(id=user_id)
        except ESUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        registration = self.get_object(event, user)
        serializer = RegistrationPresenceSerializer(registration, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @extend_schema(
        summary='Delete a registration presence',
        responses={204: None},
    )
    def delete(self, request, event_id, user_id, format=None):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user = ESUser.objects.get(id=user_id)
        except ESUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        registration = self.get_object(event, user)
        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganizerDetail(APIView):
    """
    Retrieve the organizer of an event.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, event):
        try:
            return RegistrationPresence.objects.get(event=event, type='organizer')
        except RegistrationPresence.DoesNotExist:
            raise Http404
        
    def get_orguser(self, userid):
        try:
            return ESUser.objects.get(pk=userid)
        except ESUser.DoesNotExist:
            raise Http404

    @extend_schema(
        summary='Retrieve organizer for an event',
        responses={200: RegistrationPresenceSerializer},
    )
    def get(self, request, event_id, format=None):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

        registration = self.get_object(event)
        user = self.get_orguser(registration.user)
        serializer = ESUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)