from core.models import ESUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


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
    

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=ESUser.objects.all())]
    )
    cpf = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=ESUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = ESUser
        fields = ('email', 'cpf', 'name', 'birth_date', 'phone', 'user_type', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = ESUser.objects.create(
            email=validated_data['email'],
            cpf=validated_data['cpf'],
            name=validated_data['name'],
            birth_date=validated_data['birth_date'],
            phone=validated_data['phone'],
            user_type=validated_data['user_type']
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user

