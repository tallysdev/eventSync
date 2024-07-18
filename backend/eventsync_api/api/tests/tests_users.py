from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from core.models import ESUser
from django.urls import reverse


class UserTests(APITestCase):

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
        self.admin = ESUser.objects.create_superuser(
            email="adminuser@example.com",
            password="adminpass123",
            cpf="10987654321",
            name="Admin User",
            birth_date="1990-01-01",
            phone="10987654321"
        )

    def test_register_view(self):
        url = reverse('register')
        data = {
            "email": "newuser@example.com",
            "password": "newpassword123",
            "password2": "newpassword123",
            "cpf": "23456789012",
            "name": "New User",
            "birth_date": "1995-05-05",
            "phone": "23456789012"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('email', response.data)
        self.assertIn('cpf', response.data)
        self.assertIn('name', response.data)
        self.assertIn('birth_date', response.data)
        self.assertIn('phone', response.data)

    def test_register_view_invalid_data(self):
        url = reverse('register')
        invalid_data = {
            "email": "invalid-email",
            "password": "short",
            "password2": "short",
            "cpf": "123",
            "name": "",
            "birth_date": "invalid-date",
            "phone": "12345"
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertIn('name', response.data)
        self.assertIn('birth_date', response.data)
        self.assertIn('phone', response.data)
        self.assertIn('password', response.data)

    def test_user_list_view(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('user_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_user_detail_view(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('user_detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('email', response.data)
        self.assertIn('cpf', response.data)
        self.assertIn('name', response.data)
        self.assertIn('birth_date', response.data)
        self.assertIn('phone', response.data)

    def test_user_detail_view_patch(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('user_detail', kwargs={'pk': self.user.pk})
        data = {"name": "Updated Name"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Name")

    def test_user_detail_view_delete(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('user_detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(ESUser.DoesNotExist):
            ESUser.objects.get(pk=self.user.pk)

