from rest_framework import serializers

from ..models import ChoiceModel
from ..models.ExampleModel import ExampleModel
from ..models.VoteModel import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"