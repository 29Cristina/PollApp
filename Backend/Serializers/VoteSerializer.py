from rest_framework import serializers

from ..models.VoteModel import VoteModel


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteModel
        fields = "__all__"