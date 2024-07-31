from core.models import Sponsor
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import ReadOnly
from ..serializers.sponsor_serializers import SponsorSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class SponsorListView(APIView):
    """
    List all sponsors, or create a new sponsor.
    """
    permission_classes = [IsAuthenticated | ReadOnly]
    pagination_class = CustomPageNumberPagination

    @extend_schema(
        summary='List all sponsors',
        responses={200: SponsorSerializer(many=True)},
        parameters=[
            OpenApiParameter(
                name='page', description='Page number', required=False, type=int),
            OpenApiParameter(
                name='page_size', description='Page size', required=False, type=int),
        ],
    )
    def get(self, request, format=None):
        sponsors = Sponsor.objects.all().order_by("id")
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(sponsors, request)
        serializer = SponsorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(
        summary='Create a new sponsor',
        request=SponsorSerializer,
        responses={201: SponsorSerializer},
    )
    def post(self, request, format=None):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SponsorDetailView(APIView):
    """
    Retrieve, update or delete an sponsor.
    """
    permission_classes = [IsAuthenticated | ReadOnly]

    def get_object(self, pk):
        try:
            return Sponsor.objects.get(pk=pk)
        except Sponsor.DoesNotExist:
            raise Http404

    @extend_schema(
        summary='Retrieve a sponsor',
        responses={200: SponsorSerializer},
    )
    def get(self, request, pk, format=None):
        sponsor = self.get_object(pk)
        serializer = SponsorSerializer(sponsor)
        return Response(serializer.data)

    @extend_schema(
        summary='Update a sponsor',
        request=SponsorSerializer,
        responses={200: SponsorSerializer},
    )
    def patch(self, request, pk, format=None):
        sponsor = self.get_object(pk)
        serializer = SponsorSerializer(
            sponsor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary='Delete a sponsor',
        responses={204: None},
    )
    def delete(self, request, pk, format=None):
        sponsor = self.get_object(pk)
        sponsor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
