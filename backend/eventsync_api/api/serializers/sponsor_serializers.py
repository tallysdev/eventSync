from rest_framework import serializers
from core.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['name', 'logo', 'phone', 'email', 'description']