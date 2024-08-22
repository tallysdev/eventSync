import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import Local, Event, ESUser, RegistrationPresence


class Command(BaseCommand):
    help = 'Create 5 Local and 20 Event records for testing, and create a unique user who will be the organizer for each event'

    def handle(self, *args, **kwargs):
        # Create a unique user
        user = ESUser.objects.create_user(
            email='organizer@example.com',
            password='organizerpass',
            cpf='12345678901',
            name='Event Organizer',
            birth_date='1990-01-01',
            phone='12345678901',
        )

        # Create 5 Locals
        locals_data = [
            {'local_name': 'Local A', 'street_name': 'Street A', 'street_number': '123', 'city': 'City A', 'state': 'State A', 'cep': '00000-000', 'reference': 'Reference A'},
            {'local_name': 'Local B', 'street_name': 'Street B', 'street_number': '456', 'city': 'City B', 'state': 'State B', 'cep': '11111-111', 'reference': 'Reference B'},
            {'local_name': 'Local C', 'street_name': 'Street C', 'street_number': '789', 'city': 'City C', 'state': 'State C', 'cep': '22222-222', 'reference': 'Reference C'},
            {'local_name': 'Local D', 'street_name': 'Street D', 'street_number': '101', 'city': 'City D', 'state': 'State D', 'cep': '33333-333', 'reference': 'Reference D'},
            {'local_name': 'Local E', 'street_name': 'Street E', 'street_number': '202', 'city': 'City E', 'state': 'State E', 'cep': '44444-444', 'reference': 'Reference E'},
        ]

        locals = [Local.objects.create(**data) for data in locals_data]

        # Create 20 Events
        event_statuses = ['upcoming', 'ongoing', 'completed', 'cancelled']
        event_types = ['conference', 'workshop', 'seminar', 'meetup']

        for i in range(20):
            local = random.choice(locals)
            start_date = timezone.now().date() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(1, 5))

            event = Event.objects.create(
                name=f'Event {i+1}',
                start_date=start_date,
                end_date=end_date,
                max_quantity=random.randint(10, 100),
                min_quantity=random.randint(1, 10),
                hours_quantity=random.randint(1, 8),
                description=f'Description for Event {i+1}',
                local=local,
                status=random.choice(event_statuses),
                event_type=random.choice(event_types)
            )

            # Create RegistrationPresence for the organizer
            RegistrationPresence.objects.create(
                user=user,
                event=event,
                presence=True,
                type='organizer'
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 5 locals, 20 events, and assigned an organizer to each event in your dev database'))
