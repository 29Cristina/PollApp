from django.db import models

from Backend.models.VoteModel import User


class ChoiceModel(models.Model):
    text=models.CharField()
    poll =models.ForeignKey(Poll,on_delete=models.CASCADE())

