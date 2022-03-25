from django.contrib.auth.models import User
from django.db import models

from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.PollModel import PollModel


class VoteModel(models.Model):
    choice = models.ForeignKey(ChoiceModel, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
