from core.models import RegistrationPresence

def save_current_user_registration(user, event_instance):
    if user:
        new_reg = RegistrationPresence.objects.create(
            user=user,
            event=event_instance,
            type='organizer',
            presence=True
        )
        new_reg.save()
