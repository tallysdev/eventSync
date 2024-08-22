from rest_framework import serializers
from core.models import RegistrationPresence

class RegistrationPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationPresence
        fields = '__all__'

    # def validate(self, data):
    #     # Get the user and event from either the instance or the initial data
    #     user = self.context['request'].user if self.instance is None else self.instance.user
    #     event = data.get('event', self.instance.event if self.instance else None)

    #     # Custom validation logic
    #     if RegistrationPresence.objects.filter(user=user, event=event).exists():
    #         raise serializers.ValidationError("User is already signed up for this event.")

    #     if (event.status != 'upcoming') and (event.status != 'ongoing'):
    #         raise serializers.ValidationError("You can only sign up for upcoming or ongoing events.")

    #     return data
