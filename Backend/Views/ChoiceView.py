from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins

from Backend.models.ChoiceModel import ChoiceModel
from Backend.Serializers.ChoiceSerializer import ChoiceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ChoiceList(generics.ListCreateAPIView):
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer


@api_view(['GET'])
def getChoices(request, pk):
    choices = ChoiceModel.objects.filter(poll=pk)
    serializer = ChoiceSerializer(choices, many=True)

    return Response(serializer.data)
