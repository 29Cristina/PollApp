from rest_framework import serializers
from ..models.ChoiceModel import ChoiceModel
from ..models.ExampleModel import ExampleModel

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceModel
        fields = "__all__"