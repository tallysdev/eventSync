import random

from django.core.management.base import BaseCommand
from core.models import Sponsor, Event, Sponsorship


class Command(BaseCommand):
    help = 'Create 10 Sponsorship records for testing'

    def handle(self, *args, **kwargs):

        sponsors = list(Sponsor.objects.all())
        events = list(Event.objects.all())

        if not sponsors or not events:
            self.stdout.write(self.style.ERROR(
                'Ensure there are sponsors and events in the database before running this command.'))
            return

        for i in range(10):
            sponsor = random.choice(sponsors)
            event = random.choice(events)

            Sponsorship.objects.create(
                sponsor=sponsor,
                event=event
            )

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created 10 sponsorships in your dev database'))
