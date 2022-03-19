# Create your views here.
from rest_framework import generics, viewsets, permissions


from Backend.models.PollModel import PollModel
from Backend.Serializers.PollSerializer import PollSerializer
from Backend.permissions.DeleteIfOwnerOrStaffPermission import DeleteIfOwnerOrStaffPermission


class PollList(generics.ListCreateAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
