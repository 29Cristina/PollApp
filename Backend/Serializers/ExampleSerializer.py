from rest_framework import serializers
from ..Models.ExampleModel import ExampleModel

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = "__all__"