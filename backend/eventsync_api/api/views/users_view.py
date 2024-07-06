from core.models import ESUser
from django.http import Http404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import ReadOnly
from ..serializers.auth_serializers import ESUserSerializer


class UserList(APIView):
    """
    List all users, or create a new EventSyncUser.
    """
    permission_classes = [IsAuthenticated | ReadOnly]
    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return Response("Acesso negado. É necessário autenticação para acessar este recurso.", status=status.HTTP_403_FORBIDDEN)

        users = ESUser.objects.all()
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

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ESUserSerializer(user)
        return Response(serializer.data)

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

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)