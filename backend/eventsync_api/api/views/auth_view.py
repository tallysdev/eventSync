from rest_framework import generics
from rest_framework.permissions import AllowAny
from core.models import ESUser
from ..serializers.auth_serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = ESUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
