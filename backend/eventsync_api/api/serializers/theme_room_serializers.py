from rest_framework import serializers
from core.models import ThemeRoom

class ThemeRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThemeRoom
        fields = '__all__'