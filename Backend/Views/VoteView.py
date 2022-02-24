from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from Backend.models.VoteModel import Vote
from Backend.Serializers.VoteSerializer import VoteSerializer


class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = VoteSerializer
