from django.contrib.auth.models import User
from django.db import models

from Backend.models.ChoiceModel import ChoiceModel


class VoteModel(models.Model):
    choice = models.ForeignKey(ChoiceModel, on_delete=models.CASCADE())
    voter = models.ForeignKey(User, on_delete=models.CASCADE())

    def __init__(self):
        return self.id
