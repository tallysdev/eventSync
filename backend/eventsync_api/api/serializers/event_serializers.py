from rest_framework import serializers
from core.models import Event
from .local_serializers import LocalSerializer

class EventSerializer(serializers.ModelSerializer):
    local = LocalSerializer()

    class Meta:
        model = Event
        fields = '__all__'