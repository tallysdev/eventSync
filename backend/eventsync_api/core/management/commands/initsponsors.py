from faker import Faker

from django.core.management.base import BaseCommand
from core.models import Sponsor

fake = Faker()


class Command(BaseCommand):
    help = 'Create 10 Sponsor records for testing'

    def handle(self, *args, **kwargs):

        for i in range(10):
            Sponsor.objects.create(
                name=fake.company(),
                logo=None,  # Assuming you might add logos later
                phone=fake.msisdn(),
                email=fake.email(),
                description=fake.text(max_nb_chars=200)
            )

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created 10 sponsors in your dev database'))
