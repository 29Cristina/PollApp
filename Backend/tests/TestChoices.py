from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from Backend.models.PollModel import PollModel
from Backend.models.ChoiceModel import ChoiceModel
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

client = APIClient()


class GetChoiceList(APITestCase):
    """ Test module for getting all choices (GET)"""

    def choices_get_example_list(self):
        url = reverse('choice_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetChoiceIndividual(APITestCase):
    """ Test module for getting a single choice (GET)"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.test_user = User.objects.create_user(username='testu', password='test')
        cls.poll = PollModel.objects.create(question='Intrebare', creator=cls.test_user)
        cls.choice = ChoiceModel.objects.create(text="Test Name", poll=cls.poll)

    def test_get_example_individual(self):
        url = reverse('choice_individual', kwargs={'pk': self.choice.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateChoice(APITestCase):
    """ Test module for inserting a new choice (POST) being authenticated or not"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.admin = User.objects.create_user(username='mono', password='parola')
        cls.test_user = User.objects.create_user(username='testu', password='test')
        cls.poll = PollModel.objects.create(question='Intrebare', creator=cls.test_user)
        cls.text = "Test Name"

    def test_create_choice_authenticated(self):
        data = {
            'text': self.text,
            'poll': self.poll.pk
        }
        self.client.force_authenticate(user=self.admin)

        url = reverse('choice_list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_create_choice_unauthenticated(self):
        data = {
            'text': self.text,
            'poll': self.poll.pk
        }

        url = reverse('choice_list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

