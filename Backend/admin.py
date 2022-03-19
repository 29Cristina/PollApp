from django.contrib import admin

# Register your models here.
from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.PollModel import PollModel
from Backend.models.VoteModel import VoteModel

admin.site.register(VoteModel)
admin.site.register(ChoiceModel)
admin.site.register(PollModel)