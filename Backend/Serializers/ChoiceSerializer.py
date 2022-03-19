from rest_framework import serializers
from ..models.ChoiceModel import ChoiceModel

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceModel
        fields = "__all__"