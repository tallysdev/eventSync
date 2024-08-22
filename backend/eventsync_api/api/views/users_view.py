from core.models import ESUser
from django.http import Http404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter

from ..permissions import ReadOnly
from ..serializers.auth_serializers import ESUserSerializer


class UserList(APIView):
    """
    List all users, or create a new EventSyncUser.
    """
    permission_classes = [IsAuthenticated | ReadOnly]
    pagination_class = PageNumberPagination


    @extend_schema(
        responses={200: ESUserSerializer(many=True)},
        parameters=[
            OpenApiParameter(name='page', description='Page number', required=False, type=int),
            OpenApiParameter(name='page_size', description='Page size', required=False, type=int),
        ],
    )
    def get(self, request, format=None):
        users = ESUser.objects.all().order_by("id")
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(users, request)
        serializer = ESUserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class UserDetail(APIView):
    """
    Retrieve, update or delete an ESUser.
    """
    permission_classes = [IsAuthenticated | ReadOnly]

    def get_object(self, pk) -> ESUser:
        try:
            return ESUser.objects.get(pk=pk)
        except ESUser.DoesNotExist:
            raise Http404

    @extend_schema(
        responses={200: ESUserSerializer},
    )
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ESUserSerializer(user)
        return Response(serializer.data)

    @extend_schema(
        request=ESUserSerializer,
        responses={200: ESUserSerializer},
    )
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        user_data = request.data.copy()
        serializer = ESUserSerializer(user, data=user_data, partial=True)

        if not serializer.is_valid():
            errors = serializer.errors
            for field, field_errors in errors.items():
                print(f"Error in field '{field}': {field_errors}")
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={204: None},
    )
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)