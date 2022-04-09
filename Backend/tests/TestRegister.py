from django.test import TestCase, Client

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.PollModel import PollModel
from Backend.models.VoteModel import VoteModel

client = Client()

class RegisterTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # for already existent user
        User.objects.create_user(username="existentuser", password="pass123#")

    def test_register_newuser(self):
        data = {
            'username': 'testuser',
            'password': 'pass123#',
            'password2': 'pass123#',
            'email': 'testuser@gmail.com',
            'first_name': 'First',
            'last_name': 'Last',
        }
        url = reverse('auth_register')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_alreadyexists(self):
        data = {
            'username': 'existentuser',
            'password': 'pass123#',
            'password2': 'pass123#',
            'email': 'testuser@gmail.com',
            'first_name': 'First',
            'last_name': 'Last',
        }
        url = reverse('auth_register')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

