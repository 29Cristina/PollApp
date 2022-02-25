from rest_framework import serializers

from Backend.models.PollModel import PollModel


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollModel
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['creator'] = instance.creator.username

        return representation