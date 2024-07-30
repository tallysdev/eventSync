from core.models import ESUser, Event, Local
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from ..serializers.event_serializers import EventSerializer


class EventTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = ESUser.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
            cpf="12345678901",
            name="Test User",
            birth_date="2000-01-01",
            phone="12345678901"
        )
        self.client.force_authenticate(user=self.user)
        self.local = Local.objects.create(
            street_name='Street Test',
            street_number='123',
            city='City Test',
            state='State Test',
            cep='00000-000',
            reference='Reference Test',
            local_name='Local Test'
        )
        self.event_data = {
            'name': 'Event Test',
            'start_date': '2024-07-22',
            'end_date': '2024-07-23',
            'max_quantity': 100,
            'min_quantity': 10,
            'hours_quantity': 5,
            'description': 'Event description test',
            'local': self.local,
            'status': 'upcoming',
            'event_type': 'conference'
        }
        self.event = Event.objects.create(**self.event_data)

    def test_list_events(self):
        url = reverse('event_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_create_event(self):
        url = reverse('event_list')
        data = {
            'name': 'Event Create',
            'start_date': '2024-07-24',
            'end_date': '2024-07-25',
            'max_quantity': 200,
            'min_quantity': 20,
            'hours_quantity': 10,
            'description': 'Event create description',
            'local': self.local.id,
            'status': 'upcoming',
            'event_type': 'workshop'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)
        self.assertEqual(Event.objects.last().name, 'Event Create')

    def test_retrieve_event(self):
        url = reverse('event_detail', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.event.name)

    def test_partial_update_event(self):
        url = reverse('event_detail', kwargs={'pk': self.event.pk})
        data = {'name': 'Event Partially Updated'}
        response = self.client.patch(url, data, format='json')
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # Adiciona isso para ver os erros detalhados
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, 'Event Partially Updated')

    def test_delete_event(self):
        url = reverse('event_detail', kwargs={'pk': self.event.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)
