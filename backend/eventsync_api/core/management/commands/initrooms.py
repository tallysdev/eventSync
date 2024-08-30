import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import ThemeRoom, Event

class Command(BaseCommand):
    help = 'Create 5 Local and 20 Event records for testing'

    def handle(self, *args, **kwargs):
        # Criar 5 Locais

        # Criar 20 Eventos
        event_statuses = ['upcoming', 'ongoing', 'completed', 'cancelled']
        event_types = ['conference', 'workshop', 'seminar', 'meetup']

        for i in range(20):
            start_date = timezone.now().date() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(1, 5))
            start_time= timezone.now()

            ThemeRoom.objects.create(
                event = Event.objects.get(pk=1),
                name=f'Sala Tematica {i+1}',
                speaker=f'Palestrante {i+1}',
                start_date=start_date,
                end_date=end_date,
                start_time=start_time,
                max_quantity=random.randint(10, 100),
                min_quantity=random.randint(1, 10),
                hours_quantity=random.randint(1, 8),
                description=f'Descrição da Sala {i+1}',
                local=f'Bloco A, Sala A34',
                audiences='Alunos',
                status=random.choice(event_statuses),
                event_type=random.choice(event_types)
            )

        self.stdout.write(self.style.SUCCESS('Successfully 20 rooms in your dev database event 1'))