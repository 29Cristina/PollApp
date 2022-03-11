from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.test import TestCase, Client

# la get single si delete cu individual
from rest_framework.utils import json

from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.PollModel import PollModel
from Backend.Serializers.ChoiceSerializer import ChoiceSerializer

from Backend.Serializers.PollSerializer import PollSerializer

client = Client()


class GetAllChoicesTest(TestCase):
    """ Test module for GET all Choices API """

    def setUp(self):
        self.test_user = User.objects.create_user(username='testu', password='test')
        self.poll = PollModel.objects.create(question='Intrebare', creator=self.test_user)

        self.intrebare1 = ChoiceModel.objects.create(
            text="PrimTest", poll=self.poll)
        self.intrebare2 = ChoiceModel.objects.create(
            text="Testuldoi", poll=self.poll)
        self.intrebare3 = ChoiceModel.objects.create(
            text="totlagett", poll=self.poll)

    def test_get_all_choices(self):
        # get API response
        response = client.get(reverse('choice_list'))
        # get data from db
        choices = ChoiceModel.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleChoiceTest(TestCase):
    """ Test module for GET single choice API """

    def setUp(self):
        self.test_user = User.objects.create_user(username='testu', password='test')
        self.poll = PollModel.objects.create(question='Intrebare', creator=self.test_user)
        self.intrebare1 = ChoiceModel.objects.create(
            text="PrimgettTest", poll=self.poll)
        self.intrebare2 = ChoiceModel.objects.create(
            text="Testugettldoi", poll=self.poll)
        self.intrebare3 = ChoiceModel.objects.create(
            text="totlagettul", poll=self.poll)

    def test_get_valid_single_choice(self):
        response = client.get(
            reverse('choice_individual', kwargs={'pk': self.intrebare1.pk}))
        choice = ChoiceModel.objects.get(pk=self.intrebare1.pk)
        serializer = ChoiceSerializer(choice)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_choice(self):
        response = client.get(
            reverse('choice_individual', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PostNewChoiceTest(TestCase):
    """ Test module for inserting a new choice """

    def setUp(self):
        self.test_user = User.objects.create_user(username='testu', password='test')
        self.poll = PollModel.objects.create(question='Intrebare', creator=self.test_user)

        self.serializer = PollSerializer(self.poll)

        self.valid_payload = {
            'text': 'macamplictisesc',
            'poll': self.poll
        }
        self.invalid_payload = {
            'text': '',
            'poll': self.poll
        }

    def test_create_valid_choice(self):
        print(self.serializer.data)
        response = self.client.post(reverse('choice_list'), self.valid_payload, format="json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_choice(self):
        response = client.post(
            reverse('choice_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PutSingleChoiceTest(TestCase):
    """ Test module for updating an existing choice record """

    def setUp(self):
        self.test_user = User.objects.create_user(username='testu', password='test')
        self.poll = PollModel.objects.create(question='Intrebare', creator=self.test_user)
        self.intrebare1 = ChoiceModel.objects.create(
            text="PrimgettTest", poll=self.poll)
        self.intrebare2 = ChoiceModel.objects.create(
            text="Testugettldoi", poll=self.poll)
        self.intrebare3 = ChoiceModel.objects.create(
            text="totlagettul", poll=self.poll)

        self.valid_payload = {
            'text': 'numergenimic',
            'poll': self.poll
        }
        self.invalid_payload = {
            'text': '',
            'poll': self.poll
        }

    def test_valid_update_choice(self):
        response = client.put(
            reverse('choice_individual', kwargs={'pk': self.intrebare1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_choice(self):
        response = client.put(
            reverse('choice_individual', kwargs={'pk': self.intrebare1.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleChoiceTest(TestCase):
    """ Test module for deleting an existing choice record """

    def setUp(self):
        self.test_user = User.objects.create_user(username='testu', password='test')
        self.poll = PollModel.objects.create(question='Intrebare', creator=self.test_user)
        self.intrebare1 = ChoiceModel.objects.create(
            text="PrimgettTest", poll=self.poll)
        self.intrebare2 = ChoiceModel.objects.create(
            text="Testugettldoi", poll=self.poll)
        self.intrebare3 = ChoiceModel.objects.create(
            text="totlagettul", poll=self.poll)

    def test_valid_delete_choice(self):
        response = client.delete(
            reverse('choice_individual', kwargs={'pk': self.intrebare1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_choice(self):
        response = client.delete(
            reverse('choice_individual', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


"""
class GetSingleChoiceTest(TestCase):
    def setup(self):
        test_user = User.objects.create_user(username='test', password='test')
        poll = PollModel.objects.create(question='Intrebare', creator=test_user.id)
        ChoiceModel.objects.create(text='altrandom', poll=poll)
        ChoiceModel.objects.create(text='dcfacatateachestii', poll=poll)
        self.intr=ChoiceModel.objects.create(text='ceeeee', poll=poll)
        self.valid_payload = {
            'text': 'choice_test',
            'poll': poll
        }
        self.invalid_payload = {
            'text': '',
            'poll': poll
        }

    # GET:
    def test_get_all_choices(self):
        response = self.client.get(reverse('choice_list'))
        choices = ChoiceModel.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_choice(self):
        response = client.get(
            reverse('choice_individual', kwargs={'pk': self.intr.pk}))
        choice = ChoiceModel.objects.get(pk=self.intr.pk)
        serializer = ChoiceSerializer(choice)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_choice(self):
        response = client.get(
            reverse('choice_individual', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


#
class PostSingleChoiceTest(TestCase):
    def setup(self):
        test_user = User.objects.create_user(username='test', password='test')
        poll = PollModel.objects.create(question='Intrebare', creator=test_user.id)
        self.valid_payload = {
            'text': 'choice_test',
            'poll': poll
        }
        self.invalid_payload = {
            'text': '',
            'poll': poll
        }

    def test_create_valid_choice(self):
        response = client.post(
            reverse("choice_list"),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_choice(self):
        response = client.post(
            reverse('choice_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# DELETE:
class DeleteSingleChoiceTest(TestCase):

    def setup(self):
        test_user = User.objects.create_user(username='test', password='test')
        poll = PollModel.objects.create(question='IntrebareMalefica', creator=test_user.id)
        self.choice1 = ChoiceModel.objects.create(
            text='cealegereai', poll=poll)
        self.choice2 = PollModel.objects.create(
            name='greachestie', poll=poll)

    def test_valid_delete_choice(self):
        response = self.client.delete(
            reverse('choice_individual', kwargs={'pk': self.choice1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_choice(self):
        response = self.client.delete(
            reverse('choice_individual', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

"""
