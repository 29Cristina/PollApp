from django.test import TestCase,Client

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json

from Backend.Serializers.VoteSerializer import VoteSerializer
from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.PollModel import PollModel
from Backend.models.VoteModel import VoteModel

client = Client()
class GetSingleVoteTest(TestCase):
    """ Test module for GET Votes"""
    def setUp(self):
        self.user=User.objects.create_user(username='Dorian', password='Hatz')
        self.poll = PollModel.objects.create(question= "Hello?", creator=self.user)
        self.choice = ChoiceModel.objects.create(text= "Hi", poll=self.poll)
        self.vote = VoteModel.objects.create(choice=self.choice, voter=self.user)

    def test_get_valid_single_vote(self):
        response = client.get(
            reverse('vote_individual', kwargs={'pk': self.vote.pk}))
        votes = VoteModel.objects.get(pk=self.vote.pk)
        serializer = VoteSerializer(votes)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_vote(self):
        response = client.get(
            reverse('vote_individual', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewVoteTest(TestCase):
    """ Test module for inserting a new vote"""

    def setup(self):
        user = User.objects.create_user(username='Dorian', password='Popa')
        poll = PollModel.objects.create(question='Hatz?', creator=user)
        choice = ChoiceModel.objects.create(text='Test', poll=poll)
        self.valid_payload = {
            'choice': choice,
            'voter': user
        }
        self.invalid_payload = {
            'choice': '',
            'voter': user
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_votes'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_votes'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleVoteTest(TestCase):
    """ Test module for deleting an existing vote record """

    def setUp(self):
        self.user=User.objects.create_user(username='Dorian', password='Hatz')
        self.vote = VoteModel.objects.create(
            question='Hatz?', creator=self.user
        )
    def test_valid_delete_vote(self):
        response = client.delete(
            reverse('get_delete_update_vote', kwargs={'pk': self.muffin.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_vote', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
