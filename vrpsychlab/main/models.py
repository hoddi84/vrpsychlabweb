from django.db import models
from jsonfield import JSONField

# Create your models here.

class MyModel(models.Model):
    json = JSONField()
    participantId = models.BigIntegerField(default=1)

    def __str__(self):
        return str(self.participantId)

class TestModel(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=100)

    def __str__(self):
        return str(self.number)
