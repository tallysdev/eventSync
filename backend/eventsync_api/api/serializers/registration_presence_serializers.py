from rest_framework import serializers
from core.models import RegistrationPresence

class RegistrationPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationPresence
        fields = '__all__'

    def validate(self, data):
        # Custom validation can be added here if needed
        user = data['user']
        event = data['event']

        if RegistrationPresence.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("User is already signed up for this event.")

        if (event.status != 'upcoming') and (event.status != 'ongoing'):
            print(event.status)
            raise serializers.ValidationError("You can only sign up for upcoming or ongoing events.")

        return data