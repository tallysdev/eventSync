from core.models import Sponsorship
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import ReadOnly
from ..serializers.sponsorship_serializers import SponsorshipSerializer


class SponsorShipListView(APIView):
    """
    List all sponsorships, or create a new sponsorship.
    """
    permission_classes = [IsAuthenticated | ReadOnly]
    pagination_class = PageNumberPagination

    @extend_schema(
        summary='List all sponsorships',
        responses={200: SponsorshipSerializer(many=True)},
        parameters=[
            OpenApiParameter(
                name='page', description='Page number', required=False, type=int),
            OpenApiParameter(
                name='page_size', description='Page size', required=False, type=int),
        ],
    )
    def get(self, request, format=None):
        sponsorships = Sponsorship.objects.all().order_by("id")
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(sponsorships, request)
        serializer = SponsorshipSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(
        summary='Create a new sponsorship',
        request=SponsorshipSerializer,
        responses={201: SponsorshipSerializer},
    )
    def post(self, request, format=None):
        serializer = SponsorshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SponsorShipDetailView(APIView):
    """
    Retrieve, update or delete an sponsorship.
    """
    permission_classes = [IsAuthenticated | ReadOnly]

    def get_object(self, pk):
        try:
            return Sponsorship.objects.get(pk=pk)
        except Sponsorship.DoesNotExist:
            raise Http404

    @extend_schema(
        summary='Retrieve a sponsorship',
        responses={200: SponsorshipSerializer},
    )
    def get(self, request, pk, format=None):
        sponsorship = self.get_object(pk)
        serializer = SponsorshipSerializer(sponsorship)
        return Response(serializer.data)

    @extend_schema(
        summary='Update a sponsorship',
        request=SponsorshipSerializer,
        responses={200: SponsorshipSerializer},
    )
    def patch(self, request, pk, format=None):
        sponsorship = self.get_object(pk)
        serializer = SponsorshipSerializer(
            sponsorship, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary='Delete a sponsorship',
        request=SponsorshipSerializer,
        responses={200: SponsorshipSerializer},
    )
    def delete(self, request, pk, format=None):
        sponsorship = self.get_object(pk)
        sponsorship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
