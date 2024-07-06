import csv
from django.core.management.base import BaseCommand
from eventsync_api.core.models import ESUser

class Command(BaseCommand):
    help = 'Create multiple users from a CSV file'

    # apos criar o csv muda o path no codigo
    def handle(self, *args, **kwargs):
        csv_file_path = '/path/to/your/users.csv'
        
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ESUser.objects.create_user(
                    email=row['email'],
                    password=row['password'],
                    cpf=row['cpf'],
                    name=row['name'],
                    birth_date=row['birth_date'],
                    phone=row['phone']
                )
        self.stdout.write(self.style.SUCCESS('Successfully created users from CSV file'))


