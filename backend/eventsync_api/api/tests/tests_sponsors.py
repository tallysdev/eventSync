from core.models import ESUser, Sponsor
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class SponsorTests(APITestCase):

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
        self.sponsor_data = {
            'name': 'Sponsor Test',
            'phone': '12345678901',
            'email': 'sponsor@example.com',
            'description': 'Sponsor description test'
        }
        self.sponsor = Sponsor.objects.create(**self.sponsor_data)

    def test_list_sponsors(self):
        url = reverse('sponsor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_create_sponsor(self):
        url = reverse('sponsor_list')
        data = {
            'name': 'Sponsor Create',
            'phone': '09876543210',
            'email': 'sponsor_create@example.com',
            'description': 'Sponsor create description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sponsor.objects.count(), 2)
        self.assertEqual(Sponsor.objects.last().name, 'Sponsor Create')

    def test_retrieve_sponsor(self):
        url = reverse('sponsor_detail', kwargs={'pk': self.sponsor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.sponsor.name)

    def test_partial_update_sponsor(self):
        url = reverse('sponsor_detail', kwargs={'pk': self.sponsor.pk})
        data = {'name': 'Sponsor Partially Updated'}
        response = self.client.patch(url, data, format='json')
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # Add this to see detailed errors
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sponsor.refresh_from_db()
        self.assertEqual(self.sponsor.name, 'Sponsor Partially Updated')

    def test_delete_sponsor(self):
        url = reverse('sponsor_detail', kwargs={'pk': self.sponsor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sponsor.objects.count(), 0)
