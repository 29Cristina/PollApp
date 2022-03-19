from Backend.models import PollModel
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

client=APIClient()

class TestPostPoll(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.my_user = User.objects.create_user(username='Auxiliar', password='AuxiliarPass')
        cls.test_user = User.objects.create_user(username='test', password='test')
        cls.data = {
            'question': 'test question?',
            'creator': cls.test_user.id
        }

    def test_create_poll_authenticated(self):
        data = {
            'question': 'test question?',
            'creator': self.test_user.id
        }
        self.client.force_authenticate(user=self.my_user)
        url = reverse('poll_list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_create_poll_unauthenticated(self):
        data = {
            'question': 'test question?',
            'creator': self.test_user.id
        }
        url = reverse('poll_list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
