from django.db import models

from Backend.models.PollModel import PollModel

class ChoiceModel(models.Model):
    text=models.CharField(max_length=256)
    poll =models.ForeignKey(PollModel,on_delete=models.CASCADE)

