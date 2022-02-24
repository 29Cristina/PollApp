from rest_framework import serializers

from Backend.models.PollModel import PollModel


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollModel
        fields = "__all__"
