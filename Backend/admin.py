from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from Backend.models.ChoiceModel import ChoiceModel
from Backend.models.ExampleModel import ExampleModel
from Backend.models.VoteModel import VoteModel

admin.site.register(ExampleModel)
admin.site.register(VoteModel)
admin.site.register(ChoiceModel)
=======
from Backend.models.PollModel import PollModel
from Backend.models.ExampleModel import ExampleModel

admin.site.register(ExampleModel)
admin.site.register(PollModel)
>>>>>>> master
