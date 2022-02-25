from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from Backend.models.ChoiceModel import ChoiceModel
from Backend.Serializers.ChoiceSerializer import ChoiceSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer