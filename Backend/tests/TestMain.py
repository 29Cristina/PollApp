from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TestGetMain(APITestCase):

    def test_get_choices(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
