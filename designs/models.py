from django.db import models


# Create your models here.
class player(models.Model):
    name = models.CharField(max_length=30)
    team = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    goals = models.IntegerField()
    assists = models.IntegerField()
    appearances = models.IntegerField()
    saves = models.IntegerField()

    def __str__(self):
        return self.name


class team(models.Model):
    name = models.CharField(max_length=100, default="Nismu Sports")
    played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    gf = models.IntegerField(default=0)
    ga = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    # gf = models.IntegerField()
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
