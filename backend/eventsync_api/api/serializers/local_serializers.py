from rest_framework import serializers
from core.models import Local

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['id','local_name', 'street_name', 'street_number', 'city', 'state', 'cep', 'reference']

        extra_kwargs = {
            "reference": {"required": False},
        }
