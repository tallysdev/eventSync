from rest_framework import serializers
from core.models import FormsRegister

class FormsRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormsRegister
        fields = '__all__'