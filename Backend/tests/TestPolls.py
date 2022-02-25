from Backend.models import PollModel
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class TestPostPoll(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test', password='test')
        cls.data = {
            'question': 'test question?',
            'creator': test_user.id
        }

    def test_create_poll(self):
        url = '/polls/'
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)