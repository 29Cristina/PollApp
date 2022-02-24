from rest_framework import serializers

from Backend.models.PollModel import PollModel


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollModel
        fields = "__all__"

    creator = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field = "username"
    )