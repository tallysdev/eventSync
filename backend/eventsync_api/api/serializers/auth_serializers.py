from rest_framework import serializers
from eventsync_api.core.models import ESUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ESUser
        fields = [
            'id', 'email', 'password', 'is_staff', 'is_active', 'date_joined',
            'cpf', 'name', 'birth_date', 'phone', 'user_type'
        ]

    def create(self, validated_data):
        user = ESUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            cpf=validated_data['cpf'],
            name=validated_data['name'],
            birth_date=validated_data['birth_date'],
            phone=validated_data['phone'],
            user_type=validated_data['user_type'],
            is_staff=validated_data.get('is_staff', False),
            is_active=validated_data.get('is_active', True)
        )
        return user
