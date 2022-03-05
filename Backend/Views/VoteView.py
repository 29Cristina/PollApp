from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from Backend.models.VoteModel import VoteModel
from Backend.Serializers.VoteSerializer import VoteSerializer


class VoteList(APIView):
    def get(self, request, format=None):
        votes = VoteModel.objects.all()
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = VoteModel.objects.all()
        serializer_class = VoteSerializer