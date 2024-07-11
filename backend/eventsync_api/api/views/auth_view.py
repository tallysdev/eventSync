from core.models import ESUser
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..serializers.auth_serializers import RegisterSerializer


@extend_schema(
    request=RegisterSerializer,
    responses={201: RegisterSerializer},
    description="Register a new user",
)
class RegisterView(generics.CreateAPIView):
    queryset = ESUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
