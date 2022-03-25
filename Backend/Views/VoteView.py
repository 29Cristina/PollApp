from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.VoteModel import VoteModel
from Backend.Serializers.VoteSerializer import VoteSerializer


class VoteList(APIView):
    def get(self, request, format=None):
        votes = VoteModel.objects.all()
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer=VoteSerializer(data=request.data)
        if serializer.is_valid() and not VoteModel.objects.filter(voter=request.user, poll=request.data["poll"]).exists() and ChoiceModel.objects.filter(pk=request.data["choice"], poll=request.data["poll"]).exists():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VoteModel.objects.all()
    serializer_class = VoteSerializer