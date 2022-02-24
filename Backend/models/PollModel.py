from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PollModel(models.Model):
    question = models.CharField(max_length=32)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.question
