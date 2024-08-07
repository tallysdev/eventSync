from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from core.models import Event, Sponsor, Sponsorship, ESUser, Local


class SponsorshipTests(APITestCase):

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
        self.event = Event.objects.create(
            name="Test Event",
            start_date="2023-01-01",
            end_date="2023-01-02",
            max_quantity=100,
            min_quantity=10,
            hours_quantity=8,
            description="Test Description",
            local=self.local,
        )
        self.sponsor = Sponsor.objects.create(
            name="Test Sponsor",
            phone="12345678901",
            email="sponsor@example.com",
            description="Test Description"
        )
        self.sponsorship = Sponsorship.objects.create(
            event=self.event,
            sponsor=self.sponsor
        )

    def test_list_sponsorships(self):
        url = reverse('sponsorship_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_sponsorship(self):
        url = reverse('sponsorship_list')
        data = {
            'event': self.event.id,
            'sponsor': self.sponsor.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_sponsorship(self):
        url = reverse('sponsorship_detail', args=[self.sponsorship.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_sponsorship(self):
        url = reverse('sponsorship_detail', args=[self.sponsorship.id])
        data = {
            'event': self.event.id,
            'sponsor': self.sponsor.id
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_sponsorship(self):
        url = reverse('sponsorship_detail', args=[self.sponsorship.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
