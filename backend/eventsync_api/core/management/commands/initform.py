from django.core.management.base import BaseCommand
from core.models import FormsRegister, Question, Event
import random

class Command(BaseCommand):
    help = 'Create FormsRegister and Question for testing'

    def handle(self, *args, **kwargs):        
        completed_events = Event.objects.filter(status='completed')

        if not completed_events.exists():
            self.stdout.write(self.style.WARNING('No completed events found.'))
            return

        forms_data = [
            {'name': f'Form {event.name}', 'description': f'Description for {event.name}', 'event': event, 'user_id': 1}
            for event in completed_events
        ]

        forms = [FormsRegister.objects.create(**data) for data in forms_data]

        question_types = ['Discursiva', 'Múltipla escolha', 'Objetiva']

        for i in range(len(forms) * 5):
            form = forms[i % len(forms)]
            q_type = random.choice(question_types)

            if q_type in ['Múltipla escolha', 'Objetiva']:
                num_options = random.randint(2, 10)
                options = [f"Option {j+1}" for j in range(num_options)]
            else:
                options = []

            Question.objects.create(
                text=f'Question {i+1}',
                type=q_type,
                options=options,
                form=form
            )

        created_count = 0

        for data in forms_data:
            FormsRegister.objects.create(**data)
            created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'{created_count} forms data initialized successfully.'))
