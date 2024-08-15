import random
from core.models import FormsRegister, Question, Local, Event, ESUser
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class FormsRegisterTests(APITestCase):

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
            name= 'Event Test',
            start_date= '2024-07-22',
            end_date= '2024-07-23',
            max_quantity= 100,
            min_quantity= 10,
            hours_quantity= 5,
            description= 'Event description test',
            local= self.local,
            status= 'upcoming',
            event_type= 'conference'
        )
        
        self.form_data = {
            'name': 'Form Test',
            'description': 'Form description test',
            'event': self.event,
            'user': self.user  
        }
        self.form = FormsRegister.objects.create(**self.form_data)

        self.question_types = ['Discursiva', 'Múltipla escolha', 'Objetiva']
        self.questions = []
        for _ in range(random.randint(1, 5)):
            options = []
            question_type = random.choice(self.question_types)
            
            if question_type in ['Múltipla escolha', 'Objetiva']:
                for _ in range(random.randint(2, 5)):
                    options.append(f'Option {random.randint(1, 100)}')
            
            question_data = {
                'form': self.form,
                'text': f'Question Test {random.randint(1, 100)}',
                'type': question_type,
                'options': options
            }
            question = Question.objects.create(**question_data)
            self.questions.append(question)

    def test_list_forms(self):
        url = reverse('form_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)
        
    def test_create_form_and_questions(self):
        url_form = reverse('form_list')
        data = {
            'name': 'Form Test Create',
            'description': 'Form description test create',
            'event': 1, 
            'user': 1
        }
        
        response = self.client.post(url_form, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FormsRegister.objects.count(), 2)
        self.assertEqual(FormsRegister.objects.last().name, 'Form Test Create')

        url_questions = reverse('question_list')
        questions = {
            'form': response.data['id'],
            'text': 'Question Test Create',
            'type': 'Múltipla escolha',
            'options': ['Option 1', 'Option 2']
        }
        response_questions = self.client.post(url_questions, questions, format='json')
        self.assertEqual(response_questions.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), len(self.questions) + 1)

    def test_retrieve_form(self):
        url = reverse('forms_detail', kwargs={'pk': self.form.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.form.name)

    def test_partial_update_form(self):
        url = reverse('forms_detail', kwargs={'pk': self.form.pk})
        data = {'name': 'Form Partially Updated'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.form.refresh_from_db()
        self.assertEqual(self.form.name, 'Form Partially Updated')

    def test_delete_form(self):
        url = reverse('forms_detail', kwargs={'pk': self.form.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FormsRegister.objects.count(), 0)
        self.assertEqual(Question.objects.filter(form=self.form).count(), 0)
