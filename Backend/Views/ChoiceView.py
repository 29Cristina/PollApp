from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from Backend.models.ChoiceModel import Choice
from Backend.Serializers.ChoiceSerializer import ChoiceSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer