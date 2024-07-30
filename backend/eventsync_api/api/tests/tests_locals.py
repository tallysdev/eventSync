from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from core.models import Local,ESUser

class LocalTests(APITestCase):

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
        self.local_data = {
            'street_name': 'Street Test',
            'street_number': '123',
            'city': 'City Test',
            'state': 'State Test',
            'cep': '00000-000',
            'reference': 'Reference Test',
            'local_name': 'Local Test'
        }
        self.local = Local.objects.create(**self.local_data)

    def test_list_locals(self):
        url = reverse('local_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_local(self):
        url = reverse('local_list')
        data = {
            'street_name': 'Street Create',
            'street_number': '456',
            'city': 'City Create',
            'state': 'State Create',
            'cep': '11111-111',
            'reference': 'Reference Create',
            'local_name': 'Local Create'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Local.objects.count(), 2)
        self.assertEqual(Local.objects.last().street_name, 'Street Create')

    def test_retrieve_local(self):
        url = reverse('local_detail', kwargs={'pk': self.local.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['local_name'], self.local.local_name)

    def test_update_local(self):
        url = reverse('local_detail', kwargs={'pk': self.local.pk})
        data = {
            'street_name': 'Updated Street',
            'street_number': '999',
            'city': 'Updated City',
            'state': 'Updated State',
            'cep': '12345-678',
            'reference': 'Updated Reference',
            'local_name': 'Local Updated'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.local.refresh_from_db()
        self.assertEqual(self.local.local_name, 'Local Updated')

    def test_partial_update_local(self):
        url = reverse('local_detail', kwargs={'pk': self.local.pk})
        data = {'local_name': 'Local Partially Updated'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.local.refresh_from_db()
        self.assertEqual(self.local.local_name, 'Local Partially Updated')

    def test_delete_local(self):
        url = reverse('local_detail', kwargs={'pk': self.local.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Local.objects.count(), 0)
