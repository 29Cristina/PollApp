from django.contrib.auth.models import User
from django.db import models

from Backend.models.ChoiceModel import ChoiceModel


class VoteModel(models.Model):
    choice = models.ForeignKey(ChoiceModel, related_name="choice", on_delete=models.CASCADE())
    voter = models.ForeignKey(User, related_name="voter", on_delete=models.CASCADE())

    def __init__(self):
        return self.id
