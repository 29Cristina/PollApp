from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Backend.models.ExampleModel import ExampleModel
from Backend.models.PollModel import PollModel
from Backend.Serializers.ExampleSerializer import ExampleSerializer
from Backend.Serializers.PollSerializer import PollSerializer

class PollList(APIView):
    def get(self, request, format=None):
        polls = PollModel.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollDetail(APIView):
    def get(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        poll = self.get_object(pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        pass