from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32)
    spent_money = models.IntegerField()
    gems = models.CharField(max_length=32)
    date = models.DateTimeField()

# Create your models here.
