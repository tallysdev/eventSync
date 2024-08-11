from rest_framework import generics
from core.models import FormsRegister
from ..serializers.form_serializers import FormsRegisterSerializer

class FormsRegisterList(generics.ListCreateAPIView):
    queryset = FormsRegister.objects.all()
    serializer_class = FormsRegisterSerializer

class FormsRegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormsRegister.objects.all()
    serializer_class = FormsRegisterSerializer
