from rest_framework import serializers
from ..models.ExampleModel import ExampleModel

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = "__all__"