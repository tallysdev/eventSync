from rest_framework import generics
from core.models import FormsRegister
from ..serializers.form_serializers import FormsRegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class FormsRegisterList(generics.ListCreateAPIView):
    queryset = FormsRegister.objects.all()
    serializer_class = FormsRegisterSerializer
    
    def post(self, request, format=None):
        serializer = FormsRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormsRegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormsRegister.objects.all()
    serializer_class = FormsRegisterSerializer
