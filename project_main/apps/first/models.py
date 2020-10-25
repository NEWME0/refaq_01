from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


class Record(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE, related_name='record_player')
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)
    field6 = models.CharField(max_length=100)
    field7 = models.CharField(max_length=100)
    field8 = models.CharField(max_length=100)
    field9 = models.CharField(max_length=100)
