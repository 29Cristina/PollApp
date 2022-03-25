from django.test import TestCase, Client

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.PollModel import PollModel
from Backend.models.VoteModel import VoteModel

client = Client()
class GetTestList(APITestCase):
    def test_get_vote_list(self):
        url = reverse('vote_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetTestIndividual(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user=User.objects.create_user(username="Ian",password='1234')
        cls.poll=PollModel.objects.create(question="Ocult?",creator=cls.user)
        cls.choice = ChoiceModel.objects.create(text="Azteca nu a dat banii", poll=cls.poll)
        cls.vote=VoteModel.objects.create(choice=cls.choice, voter=cls.user, poll=cls.poll)
    def test_get_vote_individual(self):
        url = reverse('vote_individual', kwargs={'pk': self.vote.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateVote(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="Ian", password='1234')
        cls.poll = PollModel.objects.create(question="Ocult?", creator=cls.user)
        cls.choice = ChoiceModel.objects.create(text="Azteca nu a dat banii", poll=cls.poll)

    def test_create_vote_authorized(self):
        data = {
            'choice': self.choice.pk,
            'voter': self.user.pk,
            'poll': self.poll.pk
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('vote_list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()

    def test_create_vote_unauthorized(self):
        data = {
            'choice': self.choice.pk,
            'voter': self.user.pk,
            'poll': self.poll.pk
        }
        url = reverse('vote_list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code,  status.HTTP_401_UNAUTHORIZED)

