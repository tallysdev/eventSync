from rest_framework import serializers
from core.models import Sponsorship


class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorship
        fields = ['event', 'sponsor']
