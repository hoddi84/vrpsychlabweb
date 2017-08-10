from django.db import models
from jsonfield import JSONField

# Create your models here.

class MyModel(models.Model):
    json = JSONField()
    participantId = models.BigIntegerField(default=1)

    def __str__(self):
        return str(self.participantId)

class VogabyggdModel(models.Model):
    jsonData = JSONField()
    participantName = models.CharField(max_length=50)
    participantId = models.BigIntegerField(default=1)

    def __str__(self):
        return self.participantName

class TestModel(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=100)

    def __str__(self):
        return str(self.number)

class NameModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
