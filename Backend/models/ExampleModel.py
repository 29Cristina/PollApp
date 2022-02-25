from django.db import models

# Create your models here.


class ExampleModel(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name