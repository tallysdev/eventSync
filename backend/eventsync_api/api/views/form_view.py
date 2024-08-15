from rest_framework import generics
from core.models import FormsRegister
from ..serializers.form_serializers import FormsRegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class FormsRegisterList(generics.ListCreateAPIView):
    queryset = FormsRegister.objects.all()
    serializer_class = FormsRegisterSerializer


class FormsRegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormsRegister.objects.all()
    serializer_class = FormsRegisterSerializer
