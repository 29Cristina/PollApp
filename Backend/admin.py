from django.contrib import admin

# Register your models here.
from Backend.models.PollModel import PollModel
from Backend.models.ExampleModel import ExampleModel

admin.site.register(ExampleModel)
admin.site.register(PollModel)