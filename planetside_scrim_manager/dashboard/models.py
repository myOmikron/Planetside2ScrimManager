from django.db import models
from django.db.models import CharField, ForeignKey


class Team(models.Model):
    team_name = CharField(default="", blank=False, max_length=255)


class Player(models.Model):
    player_name = CharField(default="", blank=False, max_length=255)
    team = ForeignKey(Team, on_delete=models.CASCADE)
