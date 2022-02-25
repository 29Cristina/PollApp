from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, permissions

from Backend.models.ExampleModel import ExampleModel
from Backend.Serializers.ExampleSerializer import ExampleSerializer


class ExampleList(generics.ListCreateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer


class ExampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer


