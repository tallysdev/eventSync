import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import Local, Event

class Command(BaseCommand):
    help = 'Create 5 Local and 20 Event records for testing'

    def handle(self, *args, **kwargs):
        # Criar 5 Locais
        locals_data = [
            {'local_name': 'Local A', 'street_name': 'Street A', 'street_number': '123', 'city': 'City A', 'state': 'State A', 'cep': '00000-000', 'reference': 'Reference A'},
            {'local_name': 'Local B', 'street_name': 'Street B', 'street_number': '456', 'city': 'City B', 'state': 'State B', 'cep': '11111-111', 'reference': 'Reference B'},
            {'local_name': 'Local C', 'street_name': 'Street C', 'street_number': '789', 'city': 'City C', 'state': 'State C', 'cep': '22222-222', 'reference': 'Reference C'},
            {'local_name': 'Local D', 'street_name': 'Street D', 'street_number': '101', 'city': 'City D', 'state': 'State D', 'cep': '33333-333', 'reference': 'Reference D'},
            {'local_name': 'Local E', 'street_name': 'Street E', 'street_number': '202', 'city': 'City E', 'state': 'State E', 'cep': '44444-444', 'reference': 'Reference E'},
        ]

        locals = [Local.objects.create(**data) for data in locals_data]

        # Criar 20 Eventos
        event_statuses = ['upcoming', 'ongoing', 'completed', 'cancelled']
        event_types = ['conference', 'workshop', 'seminar', 'meetup']

        for i in range(20):
            local = random.choice(locals)
            start_date = timezone.now().date() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(1, 5))

            Event.objects.create(
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

        self.stdout.write(self.style.SUCCESS('Successfully created 5 locals and 20 events in your dev database'))
