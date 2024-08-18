from core.models import Local
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..serializers.local_serializers import LocalSerializer
from ..permissions import ReadOnly


@extend_schema_view(
    get=extend_schema(summary='List all locais', tags=['Local']),
    post=extend_schema(summary='Create a new local', tags=['Local'])
)
class LocalListView(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated | ReadOnly]

@extend_schema_view(
    get=extend_schema(summary='Retrieve a local', tags=['Local']),
    put=extend_schema(summary='Update a local', tags=['Local']),
    delete=extend_schema(summary='Delete a local', tags=['Local'])
)
class LocalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    permission_classes = [IsAuthenticated | ReadOnly]
