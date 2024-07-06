from django.core.management.base import BaseCommand, CommandError
from core.models import ESUser

class Command(BaseCommand):
    help = 'Create a new superuser'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Superuser email')
        parser.add_argument('cpf', type=str, help='Superuser CPF')
        parser.add_argument('name', type=str, help='Superuser name')
        parser.add_argument('birth_date', type=str, help='Superuser birth date (YYYY-MM-DD)')
        parser.add_argument('phone', type=str, help='Superuser phone number')
        parser.add_argument('password', type=str, help='Superuser password')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        cpf = kwargs['cpf']
        name = kwargs['name']
        birth_date = kwargs['birth_date']
        phone = kwargs['phone']
        password = kwargs['password']

        try:
            user = ESUser.objects.create_superuser(
                email=email,
                cpf=cpf,
                name=name,
                birth_date=birth_date,
                phone=phone,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser "{email}" created successfully'))
        except Exception as e:
            raise CommandError(f'Error creating superuser: {e}')
