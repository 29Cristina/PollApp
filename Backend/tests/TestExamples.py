from django.urls import reverse
from rest_framework import status
from Backend.models.ExampleModel import ExampleModel
from rest_framework.test import APITestCase


class GetExampleList(APITestCase):
    """ Test module for getting all examples (GET)"""

    def test_get_example_list(self):
        url = reverse('example_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetExampleIndividual(APITestCase):
    """ Test module for getting a single example (GET)"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.example = ExampleModel.objects.create(name="Test Name", description="Test Description")

    def test_get_example_individual(self):
        url = reverse('example_individual', kwargs={'pk': self.example.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateExample(APITestCase):
    """ Test module for inserting a new example (POST)"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.name = "Test Name"
        cls.description = "Test Description"

    def test_create_example(self):
        data = {
            'name': self.name,
            'description': self.description
        }
        url = reverse('example_list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
