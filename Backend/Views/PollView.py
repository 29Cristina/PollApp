from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from Backend.models.ExampleModel import ExampleModel
from Backend.models.PollModel import PollModel
from Backend.Serializers.ExampleSerializer import ExampleSerializer
from Backend.Serializers.PollSerializer import PollSerializer


class PollList(generics.ListCreateAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer